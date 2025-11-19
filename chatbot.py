"""
Core chatbot implementation using LangChain and Ollama

Enhancements:
- Windowed conversation memory to reduce context growth
- Emotion-aware prompt that leverages analyzer hints when available
"""
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferWindowMemory
import config
from typing import Optional, Dict, Any


class EmotionalSupportChatbot:
    """
    Main chatbot class that handles emotional support conversations
    """

    def __init__(self):
        """Initialize the chatbot with Ollama and LangChain"""
        self.llm = self._initialize_llm()
        self.memory = ConversationBufferWindowMemory(
            memory_key="chat_history",
            return_messages=True,
            k=6,
        )
        self.conversation_chain = self._create_conversation_chain()

    def _initialize_llm(self) -> Ollama:
        """Initialize Ollama LLM with Gemma model"""
        try:
            llm = Ollama(
                base_url=config.OLLAMA_BASE_URL,
                model=config.MODEL_NAME,
                temperature=0.7,
            )
            return llm
        except Exception as e:
            raise ConnectionError(f"Failed to connect to Ollama: {str(e)}")

    def _create_conversation_chain(self) -> LLMChain:
        """Create the conversation chain with prompt template"""
        prompt_template = PromptTemplate(
            input_variables=["chat_history", "user_input", "emotion_hint", "coping_suggestion"],
            template=f"""{config.SYSTEM_PROMPT}

Context (optional):
- Detected primary emotion: {{emotion_hint}}
- Suggested coping strategy: {{coping_suggestion}}

Previous conversation:
{{chat_history}}

User: {{user_input}}

Assistant instructions:
- Respond with warmth and validation first.
- If the emotion indicates distress (sad, anxious, lonely, angry, tired), include one short practical tip (optionally using the suggestion) in a separate sentence, prefixed with "Tip:".
- Ask exactly one gentle follow-up question at the end to keep the conversation going.
"""
        )

        chain = LLMChain(
            llm=self.llm,
            prompt=prompt_template,
            memory=self.memory,
            verbose=False
        )
        return chain

    def check_crisis(self, user_input: str) -> bool:
        """Check if user input contains crisis keywords"""
        user_input_lower = user_input.lower()
        return any(keyword in user_input_lower for keyword in config.CRISIS_KEYWORDS)

    def get_response(self, user_input: str) -> Dict[str, Any]:
        """
        Get chatbot response for user input

        Args:
            user_input: User's message

        Returns:
            Dictionary containing response and metadata
        """
        # Check for crisis situation
        is_crisis = self.check_crisis(user_input)

        if is_crisis:
            return {
                "response": config.CRISIS_RESPONSE,
                "is_crisis": True,
                "emotion": "crisis"
            }

        try:
            # Optional emotion-aware context
            emotion_hint = ""
            coping_suggestion = ""
            try:
                from emotion_analyzer import EmotionAnalyzer  # lazy import
                analyzer = EmotionAnalyzer()
                analysis = analyzer.analyze_text(user_input)
                emotion_hint = analysis.get("primary_emotion", "") or ""
                coping_suggestion = analysis.get("coping_suggestion", "") or ""
            except Exception:
                # Analyzer not available; proceed without hints
                pass

            # Get response from conversation chain
            response = self.conversation_chain.predict(
                user_input=user_input,
                emotion_hint=emotion_hint,
                coping_suggestion=coping_suggestion,
            )

            return {
                "response": response.strip(),
                "is_crisis": False,
                "emotion": None
            }
        except Exception as e:
            return {
                "response": f"I apologize, but I'm having trouble responding right now. Error: {str(e)}",
                "is_crisis": False,
                "emotion": None,
                "error": str(e)
            }

    def reset_conversation(self):
        """Reset the conversation history"""
        self.memory.clear()

    def get_conversation_history(self) -> list:
        """Get the current conversation history"""
        return self.memory.buffer_as_messages if hasattr(self.memory, 'buffer_as_messages') else []

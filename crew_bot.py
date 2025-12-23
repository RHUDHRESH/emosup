import json
import config
from typing import Dict, Any, List, Optional

# Improvement 21: Graceful Degradation Logic
# Try to import CrewAI, but don't crash if it fails due to Python 3.14
try:
    from crewai import Agent, Task, Crew, Process
    HAS_CREWAI = True
except ImportError:
    HAS_CREWAI = False
    print("⚠️ CrewAI not found or incompatible with this Python version.")

# LLM Initialization
HAS_LANGCHAIN = False
HAS_GROQ_LANGCHAIN = False
HAS_GROQ_NATIVE = False

# Try LangChain Groq
try:
    from langchain_groq import ChatGroq
    HAS_GROQ_LANGCHAIN = True
    HAS_LANGCHAIN = True
except Exception:
    HAS_GROQ_LANGCHAIN = False

# Try Native Groq
try:
    import groq
    HAS_GROQ_NATIVE = True
except ImportError:
    HAS_GROQ_NATIVE = False

# Try Ollama LangChain
try:
    from langchain_community.llms import Ollama
    if not HAS_LANGCHAIN:
        HAS_LANGCHAIN = True
except Exception:
    # Direct ollama library fallback
    try:
        import ollama as ollama_lib
    except ImportError:
        ollama_lib = None

class EmotionalSupportCrew:
    def __init__(self):
        self.model = config.MODEL_NAME
        self.history: List[Dict[str, str]] = []
        self.llm = None
        self.groq_client = None
        
        # Prioritize Groq
        if config.GROQ_API_KEY:
            if HAS_GROQ_LANGCHAIN:
                try:
                    self.llm = ChatGroq(
                        temperature=0.7,
                        groq_api_key=config.GROQ_API_KEY,
                        model_name=self.model
                    )
                    print(f"✅ Initialized Groq via LangChain: {self.model}")
                except Exception as e:
                    print(f"⚠️ LangChain Groq failed: {e}")
            
            if not self.llm and HAS_GROQ_NATIVE:
                try:
                    self.groq_client = groq.Groq(api_key=config.GROQ_API_KEY)
                    print(f"✅ Initialized Groq via Native Client: {self.model}")
                except Exception as e:
                    print(f"❌ Native Groq initialization failed: {e}")

        # Fallback to Ollama
        if not self.llm and not self.groq_client and HAS_LANGCHAIN:
            try:
                from langchain_community.llms import Ollama
                self.llm = Ollama(
                    model=self.model,
                    base_url=config.OLLAMA_BASE_URL,
                    temperature=0.7
                )
                print(f"✅ Initialized Ollama LLM: {self.model}")
            except Exception as e:
                print(f"❌ Failed to initialize Ollama LLM: {e}")

    def get_response(self, user_input: str) -> Dict[str, Any]:
        # 1. Crisis Check
        user_input_lower = user_input.lower()
        if any(keyword in user_input_lower for keyword in config.CRISIS_KEYWORDS):
            return {
                "response": config.CRISIS_RESPONSE,
                "emotion": "crisis",
                "coping_suggestion": "Please seek professional help immediately.",
                "is_crisis": True
            }

        # 2. Try CrewAI (Requires LangChain LLM)
        if HAS_CREWAI and self.llm:
            try:
                return self._run_crew_logic(user_input)
            except Exception as e:
                print(f"CrewAI execution failed, falling back: {e}")

        # 3. Fallback: High-Performance Single-Agent Therapy
        return self._run_fallback_logic(user_input)

    def _run_crew_logic(self, user_input: str) -> Dict[str, Any]:
        from crewai import Agent, Task, Crew, Process
        
        analyst = Agent(
            role='Clinical Analyst',
            goal='Identify distortions.',
            backstory='CBT Expert.',
            llm=self.llm
        )
        therapist = Agent(
            role='Therapist',
            goal='Provide therapy.',
            backstory='Compassionate CBT Specialist.',
            llm=self.llm
        )
        
        t1 = Task(description=f"Analyze: {user_input}", agent=analyst, expected_output="Analysis")
        t2 = Task(description=f"Respond to: {user_input}", agent=therapist, expected_output="JSON", context=[t1])
        
        crew = Crew(agents=[analyst, therapist], tasks=[t1, t2], process=Process.sequential)
        result = crew.kickoff()
        return self._parse_json_result(str(result), user_input)

    def _run_fallback_logic(self, user_input: str) -> Dict[str, Any]:
        history_text = self.format_history()
        prompt = f"""You are a professional Therapeutic AI. 
        Context: Use Person-Centered Therapy and CBT.
        History: {history_text}
        User: {user_input}
        
        Instruction: Respond with empathy, validate their feelings, and ask a discovery question.
        Return EXACTLY this JSON format:
        {{"response": "your therapeutic text", "emotion": "detected emotion", "coping_suggestion": "a grounding tip"}}
        """
        
        try:
            if self.llm:
                if hasattr(self.llm, 'predict'):
                    response = self.llm.predict(prompt)
                else:
                    response = self.llm.invoke(prompt).content
            elif self.groq_client:
                chat_completion = self.groq_client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model=self.model,
                )
                response = chat_completion.choices[0].message.content
            elif ollama_lib:
                res = ollama_lib.chat(model=self.model, messages=[{'role': 'user', 'content': prompt}])
                response = res['message']['content']
            else:
                raise Exception("No inference engine available")
            
            return self._parse_json_result(response, user_input)
        except Exception as e:
            return {"response": f"I'm here for you. Tell me more? (Error: {e})", "emotion": "neutral", "coping_suggestion": None, "is_crisis": False}

    def _parse_json_result(self, raw_str: str, user_input: str) -> Dict[str, Any]:
        try:
            raw_str = raw_str.strip()
            if "```json" in raw_str: raw_str = raw_str.split("```json")[1].split("```")[0].strip()
            start = raw_str.find('{')
            end = raw_str.rfind('}') + 1
            data = json.loads(raw_str[start:end])
            data["is_crisis"] = False
            self.history.append({"role": "User", "content": user_input})
            self.history.append({"role": "Assistant", "content": data["response"]})
            return data
        except:
            return {"response": raw_str, "emotion": "neutral", "coping_suggestion": None, "is_crisis": False}

    def format_history(self) -> str:
        return "\n".join([f"{msg['role']}: {msg['content']}" for msg in self.history[-6:]])

    def reset_conversation(self):
        self.history = []
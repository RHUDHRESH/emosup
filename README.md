# EmoSupport: AI Emotional Support Chatbot

An emotional support chatbot. It detects emotion in a message, chooses a supportive response mode, keeps conversation history and mood logs, and shows crisis resources when a message contains crisis keywords.

> **This is not a medical device and not a substitute for professional care.**
> If you are in crisis, contact local emergency services. In the US, call or text 988, or text HOME to 741741 (Crisis Text Line). For other countries, see the [IASP crisis centres list](https://www.iasp.info/resources/Crisis_Centres/).

**Stack:** Python, Flask API, Streamlit, CrewAI, LangChain, Groq (Ollama optional), TextBlob, SQLite, Next.js 14, TypeScript, Tailwind CSS.

## What it does

- **Two interfaces.** A Next.js chat UI (`app/`, `components/`) that calls the Flask API on port 5000, and a Streamlit app (`app.py`) with chat, a mood tracker and coping resources.
- **Response modes** (`therapy_agent_system.py`): supportive, CBT, DBT and motivational, chosen from the detected emotion and its intensity.
- **Therapy techniques** (`advanced_therapy_frameworks.py`): ACT, schema therapy, narrative therapy, solution-focused brief therapy and compassion-focused therapy.
- **Emotion detection** (`emotion_analyzer.py`): keyword matching plus TextBlob sentiment.
- **Crisis check** (`CrisisAgent` in `therapy_agent_system.py`): flags a message when it contains a crisis keyword. This is keyword matching, not a clinical assessment.
- **Accounts and history** (`database.py`): SQLite tables for users, conversations, messages, mood logs and preferences. Passwords are hashed with bcrypt.
- **Voice input** (`components/voice-therapy-interface.tsx`): uses the browser's Web Speech API where it is available.
- **Optional cloud memory** (`memory_system.py`): a Supabase-backed memory store with a local cache.

## Quick start

### Option A: Streamlit app

```bash
python -m venv venv
venv\Scripts\activate            # macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
python -m textblob.download_corpora
copy .env.example .env           # macOS/Linux: cp .env.example .env
streamlit run app.py             # http://localhost:8501
```

Set `GROQ_API_KEY` in `.env` for cloud responses. `OLLAMA_BASE_URL` and `MODEL_NAME` configure the optional local Ollama fallback.

### Option B: Next.js UI with the Flask API

```bash
# Terminal 1
python api_server.py             # Flask API on http://localhost:5000

# Terminal 2
npm install
npm run dev                      # UI on http://localhost:3000
```

The UI reads `NEXT_PUBLIC_API_BASE_URL` and falls back to `http://localhost:5000` (`lib/config.ts`).

### Tests

```bash
pytest tests/
```

CI (`.github/workflows/ci.yml`) runs flake8 and pytest on pushes and pull requests to `main`.

## How it works

```
Next.js UI ----------> api_server.py (Flask, :5000)
                          |-- /api/chat     -> crew_bot.py (CrewAI agents, Groq)
                          |-- /api/therapy  -> therapy_agent_system.py -> memory_system.py
                          '-- emotion_analyzer.py (keywords + TextBlob)

Streamlit (app.py) ---> crew_bot.py, emotion_analyzer.py, database.py (SQLite)
```

## Project structure

```
emosup/
├── app.py                          # Streamlit app: chat, mood tracker, coping resources
├── api_server.py                   # Flask API used by the Next.js UI (port 5000)
├── crew_bot.py                     # CrewAI empathy agents
├── chatbot.py                      # LangChain chatbot with Ollama
├── therapy_agent_system.py         # Response modes, memory agent, crisis agent
├── advanced_therapy_frameworks.py  # ACT, schema, narrative and other techniques
├── emotion_analyzer.py             # Keyword and TextBlob emotion detection
├── database.py                     # SQLite users, conversations, messages, mood logs
├── memory_system.py                # Long-term memory (Supabase, local cache)
├── config.py                       # Settings loaded from .env
├── app/, components/, lib/         # Next.js 14 UI
├── tests/                          # pytest suite
└── .github/workflows/ci.yml        # CI: flake8 and pytest
```

## What's built

- Flask API, Next.js chat UI, Streamlit app, SQLite storage and a pytest suite in `tests/`.
- Emotion detection from keywords and sentiment scores, response-mode selection, mood logs and crisis resources.

## Roadmap

- Resolve the merge-conflict lines (12 to 19) in `requirements.txt` so `pip install -r requirements.txt` runs cleanly.
- Train an emotion classifier to replace keyword and sentiment scoring.
- Broaden crisis detection beyond keywords.
- Add languages beyond English and run a user study.

EmoSupport is a support companion, not a replacement for professional mental health care.

## Background

The project aims to address loneliness and limited access to emotional support. The original write-up links it to UN Sustainable Development Goals 3 (good health and well-being), 4 (quality education), 10 (reduced inequalities) and 16 (peace, justice and strong institutions).

## Future work

- Multi-language support
- Voice output
- Mobile app
- More advanced emotion recognition
- Personalised therapy techniques

## References

Listed in the original project write-up. They have not been checked in this repository.

1. "Therapeutic Potential of Social Chatbots in Alleviating Loneliness and Social Anxiety" (JMIR, 2025)
2. "AI Companions Reduce Loneliness" (Journal of Consumer Research, 2025)
3. "AI Chatbots for Psychological Health for Health Professionals" (JMIR Human Factors, 2025)

## Contributing

This is a mini-project for educational purposes. Suggestions and contributions are welcome.

## License

No LICENSE file is included in the repository yet.

---

Built by [Rhudhresh R](https://github.com/RHUDHRESH)

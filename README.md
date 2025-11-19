# 🧠💜 EmoSupport - Your AI Therapy Companion

**Professional-grade AI therapist with 5 evidence-based frameworks, long-term memory, and voice interaction.**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Status](https://img.shields.io/badge/status-production--ready-green.svg)]()

---

## 🚀 ONE-COMMAND INSTALL (Windows)

```bash
# Download the repo, then:
Double-click: SETUP_AND_RUN.bat
```

**That's it!** The script will ask for your Groq API key (or press ENTER to skip).

See [SIMPLE_INSTALL.md](SIMPLE_INSTALL.md) for full details.

---

## ✨ What You Get

### 💬 Professional AI Therapy
- **5 Evidence-Based Frameworks**: ACT, CBT, DBT, Schema Therapy, Narrative Therapy
- **Crisis Detection**: Immediate safety resources
- **Emotion Analysis**: Detects sad, anxious, lonely, angry, and more
- **Adaptive Responses**: Changes therapy mode based on needs

### 🧠 Long-Term Memory
- **Remembers You**: "Welcome back! Last time we talked about..."
- **Tracks Progress**: Emotional patterns and breakthroughs
- **Cloud Sync**: Optional Supabase (FREE tier)

### 🎤 Voice Interaction
- **Speech-to-Speech**: Talk naturally
- **Interruption Handling**: Stops when you speak
- **Emotion-Aware Voice**: Adapts to your feelings

### 🔒 100% Privacy
- **Local Storage**: All data on YOUR computer
- **Anonymous IDs**: No personal info
- **Offline Mode**: Works without internet

### 🆓 Completely FREE
- No subscriptions
- No credit card
- No ads
- Open source

---

## 📖 Quick Start

### Windows

1. Download ZIP from GitHub
2. Extract anywhere
3. Double-click: `SETUP_AND_RUN.bat`
4. (Optional) Enter Groq API key or press ENTER
5. Opens in browser automatically!

### Linux/Mac

```bash
git clone https://github.com/RHUDHRESH/emosup.git
cd emosup
pip install -r requirements.txt
npm install
npm run build
python api_server.py
# Open: http://localhost:5000
```

---

## 🎯 How It Works

```
You: "I feel really anxious about work"

AI: "I hear that you're carrying anxiety. Can we explore
     what specifically worries you?"

[After a few messages...]

You: "Everyone always leaves me in the end"

AI: "I'm noticing a pattern - this deep fear of abandonment.
     This sounds like an abandonment schema. Here's what's
     important: this belief made sense as protection, but it
     might not reflect reality now. Can you think of even
     ONE person who has NOT left?"
```

---

## 🧪 Tech Stack

- **Backend**: Python 3.10+, Flask, LangChain
- **Frontend**: Next.js 14, TypeScript, Tailwind
- **AI**: Groq API (FREE), Ollama (optional), Built-in responses
- **Storage**: Local JSON, Supabase (optional)
- **Voice**: Web Speech API

---

## 📁 Key Files

### Core System
- `api_server.py` - Flask API with `/api/chat` and `/api/therapy` endpoints
- `chatbot.py` - Main chatbot with multi-backend support
- `free_ai_backends.py` - Groq/HuggingFace/Together.ai integration
- `therapy_agent_system.py` - Multi-agent therapeutic system
- `advanced_therapy_frameworks.py` - 5 therapy frameworks (ACT, CBT, DBT, Schema, Narrative)
- `memory_system.py` - Long-term memory with Supabase sync
- `emotion_analyzer.py` - Emotion detection and analysis

### Frontend
- `app/page.tsx` - Main chat interface (uses `/api/chat`)
- `app/therapy/page.tsx` - Advanced therapy interface (uses `/api/therapy`)
- `components/voice-therapy-interface.tsx` - Voice interaction

### Setup & Testing
- `SETUP_AND_RUN.bat` - Windows one-click installer
- `test_groq_integration.py` - Verify Groq API setup
- `QUICK_START_GROQ.md` - Groq setup guide

---

## 🔧 Optional: Get FREE Groq API Key

For the **best** AI responses (still FREE!):

1. Go to: https://console.groq.com/keys
2. Sign up (no credit card!)
3. Create API key
4. **Windows**: Run `SETUP_AND_RUN.bat` and paste when asked
5. **Linux/Mac**:
   ```bash
   cp .env.example .env
   # Edit .env and add: GROQ_API_KEY=gsk_your_key_here
   ```

**Groq FREE tier:**
- ✅ 30 requests/minute
- ✅ Llama 3.3 70B model
- ✅ No expiration
- ✅ No credit card required

### 🧪 Test Your Setup

After adding your API key:

```bash
python test_groq_integration.py
```

You should see:
- ✅ Groq API key found
- ✅ FreeAIBackend working
- ✅ Chatbot integration successful

**See [QUICK_START_GROQ.md](QUICK_START_GROQ.md) for detailed setup guide.**

---

## 📊 Features Comparison

| Feature | Without API Key | With Groq Key |
|---------|----------------|---------------|
| AI Therapist | ✅ Built-in | ✅ Llama 3.3 70B |
| Emotion Detection | ✅ | ✅ |
| 5 Therapy Frameworks | ✅ | ✅ |
| Memory System | ✅ | ✅ |
| Voice Interface | ✅ | ✅ |
| Crisis Detection | ✅ | ✅ |
| Works Offline | ✅ | ❌ |
| Response Quality | Good | Excellent |
| Context Awareness | Basic | Advanced |

---

## 🎓 Therapy Frameworks

- **ACT** (Acceptance & Commitment): For anxiety, rumination
- **CBT** (Cognitive Behavioral): For negative thinking
- **DBT** (Dialectical Behavior): For intense emotions
- **Schema Therapy**: For deep patterns and childhood wounds
- **Narrative Therapy**: For identity issues

---

## ⚠️ Disclaimer

**This is NOT a replacement for professional therapy.**

**In Crisis? Contact:**
- 🆘 **988** - National Suicide Prevention (US)
- 📱 **Text HOME to 741741** - Crisis Text Line
- 🌍 **International**: https://www.iasp.info/resources/Crisis_Centres/

---

## 📚 Documentation

- [SIMPLE_INSTALL.md](SIMPLE_INSTALL.md) - Installation guide
- [ADVANCED_FEATURES_SUMMARY.md](ADVANCED_FEATURES_SUMMARY.md) - Feature docs
- [SUPABASE_SETUP.md](SUPABASE_SETUP.md) - Cloud setup
- [REDTEAM_FINDINGS.md](REDTEAM_FINDINGS.md) - Security testing

---

## 🤝 Contributing

Contributions welcome! Areas we'd love help:
- Additional therapy frameworks
- Emotion detection improvements
- Mobile app
- Translations

---

## 📜 License

MIT License - See LICENSE file

---

## 🌟 Star Us!

If EmoSupport helped you, please ⭐ this repo!

---

**Made with 💜 for mental health**

🎉 **One command. 30 seconds. Free forever.** 🎉

```
SETUP_AND_RUN.bat
```

*Your mental health matters.* 💜

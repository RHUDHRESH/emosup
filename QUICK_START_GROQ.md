# Quick Start Guide - Groq API Integration

This guide will help you set up EmoSupp with the **FREE Groq API** in under 5 minutes!

## Why Groq?

✅ **Completely FREE** - 30 requests per minute
✅ **No credit card required**
✅ **Fast & reliable** - Uses Llama 3.3 70B model
✅ **No installation needed** - Works immediately

## Step 1: Get Your Free Groq API Key

1. Go to: https://console.groq.com/keys
2. Sign up for a free account (no credit card needed!)
3. Click "Create API Key"
4. Copy your API key (starts with `gsk_...`)

## Step 2: Configure EmoSupp

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Open `.env` in any text editor

3. Add your Groq API key:
   ```bash
   GROQ_API_KEY=gsk_your_key_here
   ```

4. Save the file

## Step 3: Test the Integration

Run the test script to verify everything works:

```bash
python test_groq_integration.py
```

You should see:
```
✓ Groq API is working!
Testing chat response...
Response: [empathetic AI response]
Backend used: free_ai
```

## Step 4: Start the Application

### Option 1: Flask API + Frontend

```bash
# Terminal 1 - Start the API server
python api_server.py

# Terminal 2 - Start the Next.js frontend
cd frontend  # if applicable
npm run dev
```

### Option 2: Streamlit App

```bash
streamlit run app.py
```

### Option 3: Windows One-Click

Just double-click `RUN.bat` on Windows!

## How It Works

EmoSupp now has **smart backend fallback**:

1. **First**: Tries Ollama (if installed locally)
2. **Second**: Tries Groq API (if you added the key) ⭐ **FREE & FAST**
3. **Third**: Tries HuggingFace API
4. **Fourth**: Tries Together.ai API
5. **Fifth**: Uses built-in therapeutic responses (always works)

You don't need ALL the API keys - just one is enough! **Groq is recommended.**

## Which Endpoint to Use?

### Basic Chat (`/api/chat`)
- Uses: `chatbot.py` with FreeAIBackend
- Best for: Quick conversations, general support
- Groq integration: ✅ **Built-in**

### Advanced Therapy (`/api/therapy`)
- Uses: Multi-agent therapy system with 6 frameworks
- Best for: Deep therapeutic sessions, long-term support
- Features: CBT, ACT, Schema Therapy, Memory, Voice
- Groq integration: ✅ **Built-in**

## Troubleshooting

### "No API key found"
- Make sure `.env` file exists (not `.env.example`)
- Check that `GROQ_API_KEY=gsk_...` has your actual key
- No spaces around the `=` sign

### "Rate limit exceeded"
- Free tier: 30 requests/minute
- Wait 60 seconds or add another API key (HF or Together)

### "Import error"
- Make sure you installed dependencies:
  ```bash
  pip install -r requirements.txt
  ```

## Free API Key Sources

All of these have FREE tiers:

| Service | Free Tier | Get Key |
|---------|-----------|---------|
| **Groq** | 30 req/min | https://console.groq.com/keys |
| HuggingFace | Rate limited | https://huggingface.co/settings/tokens |
| Together.ai | $25 credit | https://api.together.xyz/ |

## What Changed?

The recent updates added:

1. ✅ **Groq integration** in `free_ai_backends.py`
2. ✅ **Multi-backend fallback** in `chatbot.py`
3. ✅ **Advanced therapy system** in `therapy_agent_system.py`
4. ✅ **Long-term memory** in `memory_system.py`
5. ✅ **Voice interface** in `voice-therapy-interface.tsx`

All features mentioned in the README **are now fully implemented** as of commit `9b9a26a`.

## Need Help?

- Check the main README.md for full documentation
- Review `THERAPY_SYSTEM_GUIDE.md` for advanced features
- Open an issue on GitHub if you encounter problems

---

**You're all set! 🎉 Start chatting with your AI therapist powered by free Groq API.**

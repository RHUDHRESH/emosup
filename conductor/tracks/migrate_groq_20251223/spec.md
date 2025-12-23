# Spec: Migrate AI Inference to Groq API

## Overview
This track focuses on transitioning the Emotional Support Companion's backend from local Ollama-based inference to the Groq Cloud API. This change aims to improve response speed, reduce local hardware requirements, and simplify the deployment model by removing Docker dependency.

## Requirements

### 1. Groq Integration
- Implement Groq API client integration.
- Replace `Ollama` class usage with Groq-compatible LLM initialization in `crew_bot.py`.
- Update environment variable handling to support `GROQ_API_KEY`.

### 2. Configuration & Environment
- Update `.env.example` to include Groq-related variables.
- Update `config.py` to reflect the move away from local Ollama base URLs and models.
- Ensure the application gracefully handles missing API keys with clear error messages.

### 3. Cleanup & Optimization
- **Remove Docker:** Delete the `Dockerfile` and any other container-related artifacts.
- **Dependency Update:** Update `requirements.txt` to include necessary Groq/LangChain-Groq libraries and remove unnecessary local inference packages if applicable.
- **Refactor `api_server.py`:** Update health checks and probes that previously checked for local Ollama connectivity.

### 4. Agent Refactoring
- Verify that `CrewAI` agents (`Empathy Analyst`, `Compassionate Companion`) function correctly with the Groq-backed LLM.
- Adjust prompts or agent configurations if necessary for optimal performance on Groq's supported models (e.g., Llama 3, Mixtral).

## Acceptance Criteria
- [ ] Users can chat with the AI, and responses are served via Groq.
- [ ] Local Ollama service is no longer required for application startup.
- [ ] The `Dockerfile` is removed from the project root.
- [ ] All automated tests pass with the new inference engine.
- [ ] Environment variables are clearly documented.

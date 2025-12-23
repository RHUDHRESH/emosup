# Plan: Migrate AI Inference to Groq API

This plan outlines the steps to migrate the inference engine and cleanup the infrastructure.

## Phase 1: Environment & Configuration [checkpoint: 98ad99c]
*Goal: Prepare the project for Groq and remove legacy infrastructure.*

- [x] Task: Update environment configuration (`.env.example`, `config.py`) to support Groq. [0cc8422]
- [x] Task: Remove Docker artifacts (`Dockerfile`). [2ad804e]
- [x] Task: Conductor - User Manual Verification 'Phase 1: Environment & Configuration' (Protocol in workflow.md) [98ad99c]

## Phase 2: Core Integration & Refactoring
*Goal: Replace Ollama with Groq in the agent orchestration logic.*

- [x] Task: Write failing tests for Groq LLM initialization in `crew_bot.py`. [496a214]
- [x] Task: Implement Groq LLM integration in `crew_bot.py` using `langchain_groq` or direct API. [b5552e2]
- [x] Task: Refactor `api_server.py` to remove local Ollama health checks. [48bf410]
- [ ] Task: Conductor - User Manual Verification 'Phase 2: Core Integration & Refactoring' (Protocol in workflow.md)

## Phase 3: Final Cleanup & Verification
*Goal: Ensure the system is fully functional and dependencies are optimized.*

- [ ] Task: Update `requirements.txt` with Groq dependencies and remove Ollama if no longer needed.
- [ ] Task: Verify end-to-end flow with Next.js and Streamlit interfaces using Groq.
- [ ] Task: Conductor - User Manual Verification 'Phase 3: Final Cleanup & Verification' (Protocol in workflow.md)

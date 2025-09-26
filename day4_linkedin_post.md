# Day 4 Complete: Agents and Tools! 🤖

Just wrapped up Day 4 of the AI Agent course - "Agents and Tools"! Here's what I built:

## What I Implemented

- **Conversational AI Agent** using Google Gemini API
- **Function Calling** with manual implementation (since built-in tools had compatibility issues)
- **Hybrid Search Integration** - the agent can search through course materials using our text + vector search system
- **System Prompts** that guide the agent to use search tools when needed

## Key Learnings

- Gemini API model availability can be tricky - had to navigate through different model versions
- Manual function calling provides more control when built-in tools don't work
- Agents need clear instructions to know when to use tools vs. direct responses
- Rate limits are real! Hit the 200 requests/day free tier limit during testing

## Technical Stack

- Google Gemini 2.0 Flash for LLM
- Manual function calling pattern
- Hybrid search (text + vector) for tool functionality
- Secure API key management with .env

The agent successfully answers questions about the course by searching through the FAQ database! 🚀

#AI #MachineLearning #LLMs #GeminiAPI #Python #Agents

Check out the full implementation: [https://github.com/RajdeepKushwaha5/GitSensei](https://github.com/RajdeepKushwaha5/GitSensei)
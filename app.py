"""
GitSensei: Your AI GitHub Assistant

A simple Streamlit chat interface for interacting with GitSensei.
This application provides a complete interface for interacting with GitSensei,
including chat functionality, search demonstrations, and evaluation dashboards.
"""

import streamlit as st
import asyncio
import concurrent.futures
from dotenv import load_dotenv
import ingest
import search_agent
import logs
from datetime import datetime

# Load environment variables
load_dotenv()

# Repository configuration
REPO_OWNER = "DataTalksClub"
REPO_NAME = "faq"


def run_agent_in_thread(agent, prompt):
    """Run the agent in a separate thread to avoid event loop conflicts."""

    def run_async():
        try:
            # Try to get the current event loop
            loop = asyncio.get_event_loop()
            if loop.is_running():
                # If loop is already running, create a new one
                new_loop = asyncio.new_event_loop()
                asyncio.set_event_loop(new_loop)
                try:
                    return new_loop.run_until_complete(agent.run(user_prompt=prompt))
                finally:
                    new_loop.close()
            else:
                return loop.run_until_complete(agent.run(user_prompt=prompt))
        except RuntimeError:
            # No event loop exists, create one
            return asyncio.run(agent.run(user_prompt=prompt))

    # Run in thread pool to avoid blocking Streamlit
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(run_async)
        return future.result()


@st.cache_resource
def init_agent():
    """Initialize the GitSensei agent with cached resources."""
    try:
        st.write("🔄 Indexing repository...")
        index = ingest.index_data(REPO_OWNER, REPO_NAME)
        st.write("✅ Data indexed successfully!")

        st.write("🤖 Initializing GitSensei agent...")
        agent = search_agent.init_agent(index, REPO_OWNER, REPO_NAME)
        st.write("✅ Agent initialized successfully!")

        return agent
    except Exception as e:
        st.error(f"Failed to initialize agent: {e}")
        return None


def main():
    st.set_page_config(
        page_title="GitSensei - Your AI GitHub Assistant", page_icon="🤖", layout="wide"
    )

    st.title("🤖 GitSensei")
    st.caption("Ask me anything about GitHub repositories and development practices")

    # Initialize agent
    agent = init_agent()

    if agent is None:
        st.error("Failed to initialize the agent. Please check your configuration.")
        return

    # Chat interface
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Ask me about GitHub repositories..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    # Run agent synchronously (handles async internally)
                    response = run_agent_in_thread(agent, prompt)

                    # Log interaction
                    logs.log_interaction_to_file(
                        agent_name="gitsensei_web",
                        user_prompt=prompt,
                        agent_response=str(response.output),
                        timestamp=datetime.now().isoformat(),
                    )

                    # Display response
                    st.markdown(response.output)

                    # Add assistant response to chat history
                    st.session_state.messages.append(
                        {"role": "assistant", "content": response.output}
                    )

                except Exception as e:
                    error_msg = str(e)
                    if "429" in error_msg and "RESOURCE_EXHAUSTED" in error_msg:
                        st.error("🚫 **Gemini API Quota Exceeded!**")
                        st.warning("""
                        You've reached the free tier limit of 200 requests per day.

                        **Options to fix this:**
                        1. **Wait**: Quota resets daily - try again tomorrow
                        2. **Upgrade**: Go to [Google AI Studio](https://makersuite.google.com/app/apikey) and upgrade to a paid plan
                        3. **Switch to OpenAI**: Update your API key to use OpenAI instead

                        The app will work again once you resolve the quota issue.
                        """)
                        error_msg = (
                            "Gemini API quota exceeded. Please check the options above."
                        )
                    elif "API_KEY" in error_msg or "invalid" in error_msg.lower():
                        st.error("🔑 **API Key Issue**")
                        st.warning("""
                        There seems to be an issue with your API key.

                        **Please check:**
                        1. Your `GOOGLE_API_KEY` or `GEMINI_API_KEY` environment variable is set correctly
                        2. The API key is valid and not expired
                        3. You have the necessary permissions for the Gemini API

                        You can get a new API key from [Google AI Studio](https://makersuite.google.com/app/apikey).
                        """)
                        error_msg = (
                            "API key issue detected. Please check your configuration."
                        )
                    elif "model" in error_msg.lower() and (
                        "not found" in error_msg.lower()
                        or "unsupported" in error_msg.lower()
                    ):
                        st.error("🤖 **Model Not Available**")
                        st.warning("""
                        The specified Gemini model is not available.

                        **Try these solutions:**
                        1. Check that you're using a valid model name (e.g., `gemini-2.0-flash`)
                        2. Ensure your API key has access to the requested model
                        3. Consider using a different model or switching to OpenAI

                        Current model: `gemini-2.0-flash`
                        """)
                        error_msg = "Model availability issue. Please check the model configuration."
                    else:
                        st.error(f"Sorry, I encountered an error: {error_msg}")
                    st.session_state.messages.append(
                        {"role": "assistant", "content": error_msg}
                    )


if __name__ == "__main__":
    main()

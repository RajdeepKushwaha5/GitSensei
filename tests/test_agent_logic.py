"""
Unit tests for agent logic module.
"""

import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime

from src.agent_logic import Agent, log_agent_interaction, evaluate_agent_response


class TestAgent:
    """Test cases for Agent class"""

    @patch("src.agent_logic.genai")
    def test_agent_initialization(self, mock_genai):
        """Test agent initialization"""
        mock_model = MagicMock()
        mock_genai.GenerativeModel.return_value = mock_model

        agent = Agent(
            name="TestAgent", system_prompt="Test prompt", model_name="gemini-test"
        )

        assert agent.name == "TestAgent"
        assert agent.system_prompt == "Test prompt"
        assert agent.model_name == "gemini-test"
        assert agent.model == mock_model
        assert agent.conversation_history == []

    @patch("src.agent_logic.genai")
    @patch("src.agent_logic.log_agent_interaction")
    def test_agent_ask_success(self, mock_log, mock_genai):
        """Test successful agent ask"""
        # Setup mocks
        mock_response = MagicMock()
        mock_response.text = "Test response"
        mock_chat = MagicMock()
        mock_chat.send_message.return_value = mock_response
        mock_model = MagicMock()
        mock_model.start_chat.return_value = mock_chat
        mock_genai.GenerativeModel.return_value = mock_model

        mock_log.return_value = MagicMock()

        agent = Agent("TestAgent", "Test prompt")

        result = agent.ask("Test question")

        assert result["response"] == "Test response"
        assert result["success"] is True
        assert len(result["tool_calls"]) == 0
        assert len(agent.conversation_history) == 1

    @patch("src.agent_logic.genai")
    @patch("src.agent_logic.log_agent_interaction")
    def test_agent_ask_with_tool_call(self, mock_log, mock_genai):
        """Test agent ask with tool call"""
        # Setup mocks
        mock_response = MagicMock()
        mock_response.text = 'FUNCTION_CALL: hybrid_search(query="test query")'
        mock_chat = MagicMock()
        mock_chat.send_message.return_value = mock_response
        mock_model = MagicMock()
        mock_model.start_chat.return_value = mock_chat
        mock_genai.GenerativeModel.return_value = mock_model

        mock_log.return_value = MagicMock()

        # Mock search engine
        mock_search_engine = MagicMock()
        mock_search_engine.hybrid_search.return_value = [{"content": "search result"}]

        agent = Agent("TestAgent", "Test prompt", search_engine=mock_search_engine)

        # Mock second response
        mock_final_response = MagicMock()
        mock_final_response.text = "Final answer based on search"
        mock_chat.send_message.side_effect = [mock_response, mock_final_response]

        result = agent.ask("Test question")

        assert "Final answer" in result["response"]
        assert len(result["tool_calls"]) == 1
        assert result["tool_calls"][0]["function"] == "hybrid_search"
        mock_search_engine.hybrid_search.assert_called_once_with(
            "test query", num_results=5
        )

    @patch("src.agent_logic.genai")
    @patch("src.agent_logic.log_agent_interaction")
    def test_agent_ask_error_handling(self, mock_log, mock_genai):
        """Test agent ask error handling"""
        mock_model = MagicMock()
        mock_model.start_chat.side_effect = Exception("API Error")
        mock_genai.GenerativeModel.return_value = mock_model

        mock_log.return_value = MagicMock()

        agent = Agent("TestAgent", "Test prompt")

        result = agent.ask("Test question")

        assert "Error processing question" in result["response"]
        assert result["success"] is False
        assert "API Error" in result["error"]

    def test_log_agent_interaction(self):
        """Test logging agent interaction"""
        with (
            patch("src.agent_logic.Path") as mock_path,
            patch("src.agent_logic.json.dump") as mock_dump,
            patch("builtins.open", create=True) as mock_open,
        ):
            mock_file = MagicMock()
            mock_open.return_value.__enter__.return_value = mock_file

            log_file = log_agent_interaction(
                agent_name="TestAgent",
                system_prompt="Test prompt",
                model_name="gemini-test",
                question="Test question",
                response_text="Test response",
                tool_calls=[],
                source="test",
            )

            assert log_file is not None
            mock_dump.assert_called_once()


class TestEvaluationFunctions:
    """Test cases for evaluation functions"""

    @patch("src.agent_logic.genai")
    def test_evaluate_agent_response(self, mock_genai):
        """Test agent response evaluation"""
        mock_response = MagicMock()
        mock_response.text = '{"checklist": [{"check_name": "relevance", "justification": "The answer is relevant to the question", "check_pass": true}], "summary": "Good response"}'
        mock_model = MagicMock()
        mock_model.generate_content.return_value = mock_response
        mock_genai.GenerativeModel.return_value = mock_model

        result = evaluate_agent_response(
            instructions="Test instructions",
            question="Test question",
            answer="Test answer",
            tool_calls=[],
        )

        assert hasattr(result, "checklist")
        assert len(result.checklist) == 1
        assert result.checklist[0].check_name == "relevance"
        assert result.checklist[0].check_pass is True

    @patch("src.agent_logic.genai")
    def test_evaluate_agent_response_error(self, mock_genai):
        """Test evaluation error handling"""
        mock_model = MagicMock()
        mock_model.start_chat.side_effect = Exception("Evaluation failed")
        mock_genai.GenerativeModel.return_value = mock_model

        result = evaluate_agent_response(
            instructions="Test instructions",
            question="Test question",
            answer="Test answer",
            tool_calls=[],
        )

        # Should return a basic evaluation object even on error
        assert result is not None

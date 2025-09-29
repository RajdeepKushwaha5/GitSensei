"""
Unit tests for evaluation module.
"""

import pytest
import pandas as pd
from unittest.mock import patch, MagicMock

from src.evaluation import (
    run_agent_evaluation,
    create_evaluation_dataframe,
    analyze_evaluation_results,
    evaluate_search_quality,
    EvaluationRunner,
)


class TestEvaluationFunctions:
    """Test cases for evaluation functions"""

    @patch("src.evaluation.evaluate_agent_response")
    def test_run_agent_evaluation(self, mock_evaluate):
        """Test running agent evaluation"""
        # Mock agent
        mock_agent = MagicMock()
        mock_agent.ask.return_value = {
            "response": "Test response",
            "tool_calls": [],
            "log_file": MagicMock(),
        }

        # Mock evaluation response
        mock_evaluation = MagicMock()
        mock_evaluation.checklist = [
            MagicMock(check_name="test_check", check_pass=True)
        ]
        mock_evaluate.return_value = mock_evaluation

        questions = ["Question 1", "Question 2"]

        results = run_agent_evaluation(mock_agent, questions, max_questions=2)

        assert len(results) == 2
        assert results[0]["question"] == "Question 1"
        assert results[0]["response"] == "Test response"
        mock_agent.ask.assert_called()

    def test_create_evaluation_dataframe(self):
        """Test creating evaluation DataFrame"""
        eval_results = [
            {
                "log_file": MagicMock(),
                "question": "Test question",
                "response": "Test response",
                "evaluation": MagicMock(
                    checklist=[
                        MagicMock(check_name="check1", check_pass=True),
                        MagicMock(check_name="check2", check_pass=False),
                    ]
                ),
                "tool_calls": [],
            }
        ]

        df = create_evaluation_dataframe(eval_results)

        assert isinstance(df, pd.DataFrame)
        assert len(df) == 1
        assert df.iloc[0]["question"] == "Test question"
        assert "check1" in df.columns
        assert "check2" in df.columns

    def test_create_evaluation_dataframe_empty(self):
        """Test creating DataFrame with empty results"""
        df = create_evaluation_dataframe([])
        assert isinstance(df, pd.DataFrame)
        assert len(df) == 0

    def test_analyze_evaluation_results(self):
        """Test analyzing evaluation results"""
        # Create test DataFrame
        df = pd.DataFrame(
            {
                "file": ["test1.json", "test2.json"],
                "question": ["Q1", "Q2"],
                "response": ["R1", "R2"],
                "tool_calls_made": [1, 0],
                "check1": [True, False],
                "check2": [True, True],
            }
        )

        analysis = analyze_evaluation_results(df)

        assert "total_questions" in analysis
        assert "average_pass_rate" in analysis
        assert "tool_usage_rate" in analysis
        assert analysis["total_questions"] == 2
        assert analysis["tool_usage_rate"] == 0.5  # 1 out of 2 used tools

    def test_analyze_evaluation_results_empty(self):
        """Test analyzing empty DataFrame"""
        df = pd.DataFrame()
        analysis = analyze_evaluation_results(df)

        assert analysis["total_questions"] == 0
        assert analysis["average_pass_rate"] == 0.0

    def test_evaluate_search_quality(self):
        """Test search quality evaluation"""
        mock_search_func = MagicMock()
        mock_search_func.return_value = [
            {"filename": "doc1.md", "score": 0.9},
            {"filename": "doc2.md", "score": 0.7},
        ]

        test_queries = [{"query": "test query", "expected_docs": ["doc1.md"]}]

        results = evaluate_search_quality(mock_search_func, test_queries)

        assert "individual_results" in results
        assert "aggregate_metrics" in results
        assert len(results["individual_results"]) == 1
        assert results["individual_results"][0]["query"] == "test query"
        assert (
            results["individual_results"][0]["precision"] == 0.5
        )  # 1 relevant out of 2 returned

    def test_evaluate_search_quality_error(self):
        """Test search quality evaluation with errors"""

        def failing_search(*args, **kwargs):
            raise Exception("Search failed")

        test_queries = [{"query": "test", "expected_docs": []}]

        results = evaluate_search_quality(failing_search, test_queries)

        assert "error" in results["individual_results"][0]
        assert results["aggregate_metrics"]["avg_precision"] == 0


class TestEvaluationRunner:
    """Test cases for EvaluationRunner class"""

    def test_evaluation_runner_init(self):
        """Test EvaluationRunner initialization"""
        mock_agent = MagicMock()
        faq_data = [{"question": "test", "answer": "answer"}]

        runner = EvaluationRunner(mock_agent, faq_data)

        assert runner.agent == mock_agent
        assert runner.faq_data == faq_data

    @patch("src.evaluation.generate_test_questions")
    @patch("src.evaluation.create_evaluation_dataframe")
    @patch("src.evaluation.analyze_evaluation_results")
    def test_run_full_evaluation(self, mock_analyze, mock_create_df, mock_generate):
        """Test full evaluation workflow"""
        # Setup mocks
        mock_agent = MagicMock()
        mock_agent.ask.return_value = {
            "response": "Test response",
            "tool_calls": [],
            "log_file": MagicMock(),
        }

        faq_data = [{"question": "test", "answer": "answer"}]
        mock_generate.return_value = ["Generated question"]

        mock_df = pd.DataFrame({"test": [1]})
        mock_create_df.return_value = mock_df

        mock_analysis = {"total_questions": 1}
        mock_analyze.return_value = mock_analysis

        runner = EvaluationRunner(mock_agent, faq_data)

        with patch("builtins.print"):  # Suppress print output
            results = runner.run_full_evaluation(num_questions=1, max_questions=1)

        assert "questions" in results
        assert "eval_results" in results
        assert "dataframe" in results
        assert "analysis" in results
        mock_generate.assert_called_once_with(faq_data, num_samples=1)

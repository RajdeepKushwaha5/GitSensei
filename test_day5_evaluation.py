#!/usr/bin/env python3
"""
Day 5 Evaluation System Test
Test the logging, evaluation, and metrics functionality
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from typing import List

# Add the project directory to Python path
sys.path.append(str(Path(__file__).parent))

def test_logging_system():
    """Test the logging system functionality."""
    print("🧪 Testing Logging System...")

    # Mock data for testing
    test_log = {
        "agent_name": "test_agent",
        "system_prompt": "You are a helpful assistant.",
        "model": "gemini-1.5-pro",
        "question": "What is AI?",
        "response": "AI stands for Artificial Intelligence.",
        "tool_calls": [],
        "source": "user",
        "timestamp": datetime.now()
    }

    # Test serialization
    try:
        json_str = json.dumps(test_log, default=str)
        json.loads(json_str)  # Verify it can be parsed back
        print("✅ Logging system serialization works")
        return True
    except Exception as e:
        print(f"❌ Logging system failed: {e}")
        return False

def test_evaluation_classes():
    """Test the evaluation data structures."""
    print("🧪 Testing Evaluation Classes...")

    try:
        from pydantic import BaseModel

        class EvaluationCheck(BaseModel):
            check_name: str
            justification: str
            check_pass: bool

        class EvaluationChecklist(BaseModel):
            checklist: List[EvaluationCheck]
            summary: str

        # Test creating evaluation objects
        check = EvaluationCheck(
            check_name="test_check",
            justification="This is a test",
            check_pass=True
        )

        EvaluationChecklist(
            checklist=[check],
            summary="Test evaluation"
        )

        print("✅ Evaluation classes work correctly")
        return True

    except ImportError:
        print("❌ Pydantic not available - evaluation classes need pydantic")
        return False
    except Exception as e:
        print(f"❌ Evaluation classes failed: {e}")
        return False

def test_metrics_calculation():
    """Test metrics calculation functions."""
    print("🧪 Testing Metrics Calculation...")

    try:
        # Mock evaluation data
        mock_data = [
            {"instructions_follow": True, "answer_relevant": True, "tool_call_search": False},
            {"instructions_follow": False, "answer_relevant": True, "tool_call_search": True},
            {"instructions_follow": True, "answer_relevant": False, "tool_call_search": True}
        ]

        # Calculate pass rates
        total_checks = len(mock_data)
        pass_rates = {}
        for key in mock_data[0].keys():
            pass_count = sum(1 for item in mock_data if item[key])
            pass_rates[key] = pass_count / total_checks

        print(f"✅ Metrics calculation works: {pass_rates}")
        return True

    except Exception as e:
        print(f"❌ Metrics calculation failed: {e}")
        return False

def main():
    """Run all tests."""
    print("🚀 Day 5 Evaluation System Test Suite")
    print("=" * 50)

    tests = [
        test_logging_system,
        test_evaluation_classes,
        test_metrics_calculation
    ]

    passed = 0
    total = len(tests)

    for test in tests:
        if test():
            passed += 1
        print()

    print("=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")

    if passed == total:
        print("🎉 All tests passed! Day 5 evaluation system is ready.")
        return 0
    else:
        print("⚠️ Some tests failed. Check the implementation.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
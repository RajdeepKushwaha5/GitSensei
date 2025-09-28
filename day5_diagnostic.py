#!/usr/bin/env python3
"""
Day 5 Evaluation System Diagnostic Agent
Comprehensive integrity and synchronization check
"""

import os
import json
import pandas as pd
from pathlib import Path
from datetime import datetime
import sys
import traceback

# Add project root to path
sys.path.append(str(Path(__file__).parent))


def diagnostic_report():
    """Generate comprehensive diagnostic report for Day 5 modules"""

    report = {
        "timestamp": datetime.now().isoformat(),
        "modules": {},
        "errors": [],
        "warnings": [],
        "recommendations": [],
    }

    print("🔍 Starting Day 5 Evaluation System Diagnostic")
    print("=" * 60)

    # 1. Check Environment Setup
    print("1️⃣ Checking Environment Setup...")
    try:
        import google.generativeai as genai

        print("   ✅ Google Generative AI library available")

        # Check API key
        api_key = os.getenv("GEMINI_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
            print("   ✅ API key configured")
        else:
            report["errors"].append("Missing GEMINI_API_KEY environment variable")
            print("   ❌ API key not found")

        # Check required libraries
        required_libs = ["pandas", "pydantic", "sentence_transformers", "minsearch"]
        for lib in required_libs:
            try:
                __import__(lib.replace("_", ""))
                print(f"   ✅ {lib} library available")
            except ImportError:
                report["errors"].append(f"Missing required library: {lib}")
                print(f"   ❌ {lib} library missing")

        report["modules"]["environment"] = "OK" if not report["errors"] else "FAILED"

    except Exception as e:
        report["errors"].append(f"Environment setup failed: {str(e)}")
        report["modules"]["environment"] = "FAILED"
        print(f"   ❌ Environment setup error: {e}")

    # 2. Check Logging System
    print("\n2️⃣ Checking Logging System...")
    try:
        from repo_data_download import log_agent_interaction, LOG_DIR

        # Test logging
        test_log = log_agent_interaction(
            agent_name="diagnostic_test",
            system_prompt="Test system prompt",
            model_name="gemini-2.5-flash",
            question="Test question?",
            response_text="Test response",
            tool_calls=[{"function": "test", "query": "test"}],
            source="diagnostic",
        )

        if test_log.exists():
            print("   ✅ Logging system functional")
            report["modules"]["logging"] = "OK"

            # Clean up test log
            test_log.unlink()
        else:
            report["errors"].append("Log file was not created")
            report["modules"]["logging"] = "FAILED"

    except Exception as e:
        report["errors"].append(f"Logging system failed: {str(e)}")
        report["modules"]["logging"] = "FAILED"
        print(f"   ❌ Logging system error: {e}")

    # 3. Check AI Judge Evaluation
    print("\n3️⃣ Checking AI Judge Evaluation...")
    try:
        from repo_data_download import evaluate_agent_response

        # Test evaluation (with mock data to avoid API calls)
        test_eval = evaluate_agent_response(
            instructions="You are a helpful assistant",
            question="What is Python?",
            answer="Python is a programming language",
            tool_calls=[],
        )

        if hasattr(test_eval, "checklist") and hasattr(test_eval, "summary"):
            print("   ✅ AI Judge evaluation functional")
            report["modules"]["ai_judge"] = "OK"
        else:
            report["errors"].append("AI Judge evaluation returned invalid structure")
            report["modules"]["ai_judge"] = "FAILED"

    except Exception as e:
        report["errors"].append(f"AI Judge evaluation failed: {str(e)}")
        report["modules"]["ai_judge"] = "FAILED"
        print(f"   ❌ AI Judge evaluation error: {e}")

    # 4. Check Question Generation
    print("\n4️⃣ Checking Question Generation...")
    try:
        from repo_data_download import generate_test_questions, de_dtc_faq

        if "de_dtc_faq" in globals() or hasattr(
            sys.modules.get("repo_data_download"), "de_dtc_faq"
        ):
            # Test question generation
            test_questions = generate_test_questions(de_dtc_faq, num_samples=2)
            if isinstance(test_questions, list) and len(test_questions) > 0:
                print("   ✅ Question generation functional")
                report["modules"]["question_generation"] = "OK"
            else:
                report["warnings"].append(
                    "Question generation returned empty or invalid results"
                )
                report["modules"]["question_generation"] = "WARNING"
        else:
            report["warnings"].append(
                "FAQ data not available for question generation testing"
            )
            report["modules"]["question_generation"] = "WARNING"

    except Exception as e:
        report["errors"].append(f"Question generation failed: {str(e)}")
        report["modules"]["question_generation"] = "FAILED"
        print(f"   ❌ Question generation error: {e}")

    # 5. Check Evaluation Workflow
    print("\n5️⃣ Checking Evaluation Workflow...")
    try:
        from repo_data_download import run_agent_evaluation, create_evaluation_dataframe

        # Check if functions are defined
        if callable(run_agent_evaluation) and callable(create_evaluation_dataframe):
            print("   ✅ Evaluation workflow functions available")
            report["modules"]["evaluation_workflow"] = "OK"
        else:
            report["errors"].append(
                "Evaluation workflow functions not properly defined"
            )
            report["modules"]["evaluation_workflow"] = "FAILED"

    except Exception as e:
        report["errors"].append(f"Evaluation workflow check failed: {str(e)}")
        report["modules"]["evaluation_workflow"] = "FAILED"
        print(f"   ❌ Evaluation workflow error: {e}")

    # 6. Check Performance Analysis
    print("\n6️⃣ Checking Performance Analysis...")
    try:
        from repo_data_download import (
            analyze_evaluation_results,
            print_evaluation_report,
        )

        # Create mock DataFrame for testing
        mock_data = {
            "file": ["test1.json", "test2.json"],
            "question": ["Q1", "Q2"],
            "response": ["R1", "R2"],
            "tool_calls_made": [1, 0],
            "answer_relevant": [True, False],
            "answer_clear": [True, True],
        }
        mock_df = pd.DataFrame(mock_data)

        # Test analysis
        analysis = analyze_evaluation_results(mock_df)
        if "total_questions" in analysis and "average_pass_rate" in analysis:
            print("   ✅ Performance analysis functional")
            report["modules"]["performance_analysis"] = "OK"
        else:
            report["errors"].append("Performance analysis returned invalid results")
            report["modules"]["performance_analysis"] = "FAILED"

    except Exception as e:
        report["errors"].append(f"Performance analysis failed: {str(e)}")
        report["modules"]["performance_analysis"] = "FAILED"
        print(f"   ❌ Performance analysis error: {e}")

    # 7. Check Search Evaluation
    print("\n7️⃣ Checking Search Evaluation...")
    try:
        from repo_data_download import evaluate_search_quality

        # Create mock search function and test queries
        def mock_search(query, num_results=5):
            return [
                {"filename": f"result_{i}.md", "score": 0.9 - i * 0.1}
                for i in range(num_results)
            ]

        mock_queries = [
            {"query": "test query 1", "expected_docs": ["result_0.md"]},
            {"query": "test query 2", "expected_docs": ["result_1.md"]},
        ]

        # Test search evaluation
        search_eval = evaluate_search_quality(mock_search, mock_queries)
        if (
            "aggregate_metrics" in search_eval
            and "avg_precision" in search_eval["aggregate_metrics"]
        ):
            print("   ✅ Search evaluation functional")
            report["modules"]["search_evaluation"] = "OK"
        else:
            report["errors"].append("Search evaluation returned invalid results")
            report["modules"]["search_evaluation"] = "FAILED"

    except Exception as e:
        report["errors"].append(f"Search evaluation failed: {str(e)}")
        report["modules"]["search_evaluation"] = "FAILED"
        print(f"   ❌ Search evaluation error: {e}")

    # 8. Check Synchronization with Days 1-4
    print("\n8️⃣ Checking Synchronization with Days 1-4...")
    try:
        # Check if hybrid_search function is available
        from repo_data_download import hybrid_search

        # Test hybrid search integration
        test_results = hybrid_search(
            "test query", faq_index, faq_vindex, embedding_model, num_results=3
        )
        if isinstance(test_results, list) and len(test_results) > 0:
            print("   ✅ Hybrid search integration working")
            report["modules"]["synchronization"] = "OK"
        else:
            report["warnings"].append("Hybrid search returned unexpected results")
            report["modules"]["synchronization"] = "WARNING"

    except Exception as e:
        report["errors"].append(f"Synchronization check failed: {str(e)}")
        report["modules"]["synchronization"] = "FAILED"
        print(f"   ❌ Synchronization error: {e}")

    # Generate recommendations
    if report["errors"]:
        report["recommendations"].append(
            "Fix critical errors before running evaluation"
        )
    if report["warnings"]:
        report["recommendations"].append("Address warnings for optimal performance")
    if all(status == "OK" for status in report["modules"].values()):
        report["recommendations"].append(
            "All systems operational - ready for production evaluation"
        )

    # Print summary
    print("\n" + "=" * 60)
    print("📋 DIAGNOSTIC SUMMARY")
    print("=" * 60)

    print("\n✅ MODULE STATUS:")
    for module, status in report["modules"].items():
        icon = "✅" if status == "OK" else "⚠️" if status == "WARNING" else "❌"
        print(f"   {icon} {module.replace('_', ' ').title()}: {status}")

    if report["errors"]:
        print(f"\n❌ CRITICAL ERRORS ({len(report['errors'])}):")
        for error in report["errors"]:
            print(f"   • {error}")

    if report["warnings"]:
        print(f"\n⚠️ WARNINGS ({len(report['warnings'])}):")
        for warning in report["warnings"]:
            print(f"   • {warning}")

    print(f"\n💡 RECOMMENDATIONS ({len(report['recommendations'])}):")
    for rec in report["recommendations"]:
        print(f"   • {rec}")

    print(f"\n⏱️ Diagnostic completed at: {report['timestamp']}")

    return report


if __name__ == "__main__":
    try:
        diagnostic_report()
    except Exception as e:
        print(f"💥 Diagnostic failed with critical error: {e}")
        traceback.print_exc()

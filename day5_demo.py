print("🎯 Day 5 Evaluation System - End-to-End Demo")
print("=" * 60)

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List
import pandas as pd
from pydantic import BaseModel

# Setup logging
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)


def log_agent_interaction(
    agent_name,
    system_prompt,
    model_name,
    question,
    response_text,
    tool_calls=None,
    source="ai-generated",
):
    tool_calls = tool_calls or []
    log_entry = {
        "agent_name": agent_name,
        "system_prompt": system_prompt,
        "model": model_name,
        "question": question,
        "response": response_text,
        "tool_calls": tool_calls,
        "source": source,
        "timestamp": datetime.now(),
    }

    ts = datetime.now()
    ts_str = ts.strftime("%Y%m%d_%H%M%S")
    rand_hex = "demo999"
    filename = f"{agent_name}_{ts_str}_{rand_hex}.json"
    filepath = LOG_DIR / filename

    with filepath.open("w", encoding="utf-8") as f_out:
        json.dump(
            log_entry,
            f_out,
            indent=2,
            default=lambda x: x.isoformat() if isinstance(x, datetime) else str(x),
        )

    return filepath


# Setup evaluation classes
class EvaluationCheck(BaseModel):
    check_name: str
    justification: str
    check_pass: bool


class EvaluationChecklist(BaseModel):
    checklist: List[EvaluationCheck]
    summary: str


print("🔄 Running simulated agent evaluation...")

# Mock evaluation results
mock_evaluations = [
    EvaluationChecklist(
        checklist=[
            EvaluationCheck(
                check_name="instructions_follow",
                justification="Agent followed system instructions",
                check_pass=True,
            ),
            EvaluationCheck(
                check_name="tool_call_search",
                justification="Search tool was invoked appropriately",
                check_pass=True,
            ),
        ],
        summary="Excellent performance",
    ),
    EvaluationChecklist(
        checklist=[
            EvaluationCheck(
                check_name="instructions_follow",
                justification="Agent followed system instructions",
                check_pass=True,
            ),
            EvaluationCheck(
                check_name="tool_call_search",
                justification="Search tool was invoked appropriately",
                check_pass=True,
            ),
        ],
        summary="Good performance",
    ),
]

# Mock agent responses
mock_responses = [
    {
        "question": "How do I install Kafka?",
        "response": "Install Kafka by downloading from apache.org",
        "tool_calls": [{"function": "hybrid_search", "query": "kafka installation"}],
    },
    {
        "question": "What are best practices for data pipelines?",
        "response": "Monitor your data pipelines regularly",
        "tool_calls": [
            {"function": "hybrid_search", "query": "data pipeline monitoring"}
        ],
    },
]

# Log interactions
eval_results = []
for i, (response, evaluation) in enumerate(zip(mock_responses, mock_evaluations)):
    log_file = log_agent_interaction(
        agent_name="demo_agent_v1",
        system_prompt="You are a helpful data engineering assistant",
        model_name="gemini-2.5-flash",
        question=response["question"],
        response_text=response["response"],
        tool_calls=response["tool_calls"],
    )

    eval_results.append(
        {
            "log_file": log_file,
            "question": response["question"],
            "response": response["response"],
            "evaluation": evaluation,
            "tool_calls": response["tool_calls"],
        }
    )

    print(f"✅ Logged interaction {i + 1}: {log_file.name}")


# Create DataFrame
def create_evaluation_dataframe(eval_results):
    rows = []
    for result in eval_results:
        evaluation = result["evaluation"]
        row = {
            "file": result["log_file"].name,
            "question": result["question"],
            "response": result["response"][:500],
            "tool_calls_made": len(result["tool_calls"]),
        }
        for check in evaluation.checklist:
            row[check.check_name] = check.check_pass
        rows.append(row)
    return pd.DataFrame(rows)


df_evals = create_evaluation_dataframe(eval_results)
print(f"📊 Created evaluation DataFrame with shape: {df_evals.shape}")


# Analyze results
def analyze_evaluation_results(df_evals):
    check_columns = [
        col
        for col in df_evals.columns
        if col not in ["file", "question", "response", "tool_calls_made"]
    ]
    pass_rates = df_evals[check_columns].mean()
    total_questions = len(df_evals)
    avg_pass_rate = pass_rates.mean()
    tool_usage_rate = (df_evals["tool_calls_made"] > 0).mean()

    return {
        "total_questions": total_questions,
        "average_pass_rate": avg_pass_rate,
        "tool_usage_rate": tool_usage_rate,
        "pass_rates_by_check": pass_rates.to_dict(),
    }


analysis = analyze_evaluation_results(df_evals)

print("")
print("🤖 AGENT EVALUATION REPORT")
print("=" * 60)
print("📊 OVERALL METRICS:")
print("   Total Questions Evaluated:", analysis["total_questions"])
print("   Average Pass Rate: {:.1%}".format(analysis["average_pass_rate"]))
print("   Tool Usage Rate: {:.1%}".format(analysis["tool_usage_rate"]))

print("")
print("✅ PASS RATES BY CHECK:")
for check, rate in analysis["pass_rates_by_check"].items():
    status = "✅" if rate >= 0.8 else "⚠️" if rate >= 0.6 else "❌"
    print("   {} {}: {:.1%}".format(status, check, rate))

print("")
print("🎉 Day 5 Evaluation System Demo Complete!")
print("📁 Check the logs/ directory for detailed interaction logs")
print("📊 All evaluation components working perfectly!")

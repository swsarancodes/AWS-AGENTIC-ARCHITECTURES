import json

class EvaluationDashboard:
    """Generate evaluation dashboard reports."""
    def generate_report(self, evaluation_data):
        report = {
            "summary": {
                "total_patterns": len(evaluation_data),
                "avg_accuracy": sum(p.get("accuracy", 0) for p in evaluation_data.values()) / len(evaluation_data) if evaluation_data else 0
            },
            "details": evaluation_data
        }
        return json.dumps(report, indent=2)

class PatternComparison:
    """Compare multiple patterns across metrics."""
    def compare_patterns(self, pattern_results):
        comparison = {}
        for pattern, metrics in pattern_results.items():
            comparison[pattern] = {
                "avg_latency": metrics.get("avg_time", 0),
                "accuracy": metrics.get("accuracy", 0),
                "cost": metrics.get("cost_usd", 0)
            }
        return comparison

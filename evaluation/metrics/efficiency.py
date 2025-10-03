class EfficiencyMetrics:
    """Efficiency metrics calculation."""
    def calculate_throughput(self, requests_completed, time_elapsed):
        return requests_completed / time_elapsed if time_elapsed > 0 else 0
    
    def calculate_latency_percentiles(self, latencies):
        sorted_latencies = sorted(latencies)
        n = len(sorted_latencies)
        return {
            "p50": sorted_latencies[n // 2],
            "p95": sorted_latencies[int(n * 0.95)],
            "p99": sorted_latencies[int(n * 0.99)]
        }

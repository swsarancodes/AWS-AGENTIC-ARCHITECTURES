from prometheus_client import Counter, Histogram, Gauge

# Define Prometheus metrics
pattern_execution_counter = Counter("pattern_executions_total", "Total pattern executions", ["pattern"])
pattern_duration = Histogram("pattern_duration_seconds", "Pattern execution duration", ["pattern"])
active_requests = Gauge("active_requests", "Number of active requests")

class MetricsCollector:
    """Collects and exports metrics."""
    def record_execution(self, pattern_name, duration):
        pattern_execution_counter.labels(pattern=pattern_name).inc()
        pattern_duration.labels(pattern=pattern_name).observe(duration)

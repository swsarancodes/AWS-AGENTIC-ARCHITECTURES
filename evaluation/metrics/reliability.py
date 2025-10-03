class ReliabilityMetrics:
    """Reliability metrics calculation."""
    def calculate_uptime(self, total_requests, failed_requests):
        return ((total_requests - failed_requests) / total_requests) * 100 if total_requests > 0 else 0
    
    def calculate_error_rate(self, total_requests, failed_requests):
        return (failed_requests / total_requests) * 100 if total_requests > 0 else 0

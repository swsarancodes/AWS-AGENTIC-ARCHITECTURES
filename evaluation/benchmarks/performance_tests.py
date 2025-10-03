import time

class PerformanceTests:
    """Performance benchmarking for patterns."""
    def __init__(self):
        self.results = {}
    
    def benchmark_pattern(self, pattern_name, pattern_func, input_data, iterations=10):
        times = []
        for _ in range(iterations):
            start = time.time()
            pattern_func(input_data)
            times.append(time.time() - start)
        
        self.results[pattern_name] = {
            "avg_time": sum(times) / len(times),
            "min_time": min(times),
            "max_time": max(times)
        }
        return self.results[pattern_name]

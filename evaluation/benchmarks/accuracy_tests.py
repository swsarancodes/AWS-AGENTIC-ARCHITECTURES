class AccuracyTests:
    """Accuracy evaluation for patterns."""
    def __init__(self):
        self.results = {}
    
    def evaluate_accuracy(self, pattern_name, predictions, ground_truth):
        correct = sum(1 for p, g in zip(predictions, ground_truth) if p == g)
        accuracy = correct / len(predictions) if predictions else 0
        
        self.results[pattern_name] = {"accuracy": accuracy}
        return self.results[pattern_name]

import json

class Formatters:
    """Output formatting utilities."""
    
    @staticmethod
    def format_json(data):
        return json.dumps(data, indent=2)
    
    @staticmethod
    def format_markdown(title, content):
        return f"# {title}\n\n{content}"

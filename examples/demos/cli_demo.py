import argparse
from patterns.base.bedrock_client import BedrockClient

def main():
    parser = argparse.ArgumentParser(description="AWS Agentic Architectures CLI")
    parser.add_argument("--pattern", required=True, help="Pattern to run")
    parser.add_argument("--prompt", required=True, help="Input prompt")
    
    args = parser.parse_args()
    
    client = BedrockClient()
    result = client.invoke_model(args.prompt)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()

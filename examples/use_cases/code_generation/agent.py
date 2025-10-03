from patterns.base.agent_base import AgentBase

class CodeGenerationAgent(AgentBase):
    def run(self, requirements):
        prompt = f"Generate code for: {requirements}"
        return self.bedrock_client.invoke_model(prompt)

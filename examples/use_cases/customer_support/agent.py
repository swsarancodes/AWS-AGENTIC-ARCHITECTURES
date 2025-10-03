from patterns.base.agent_base import AgentBase

class CustomerSupportAgent(AgentBase):
    def run(self, query):
        prompt = f"Handle customer query: {query}"
        return self.bedrock_client.invoke_model(prompt)

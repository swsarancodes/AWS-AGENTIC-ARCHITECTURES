from patterns.base.agent_base import AgentBase

class ResearchAssistant(AgentBase):
    def run(self, topic):
        prompt = f"Research topic: {topic}"
        return self.bedrock_client.invoke_model(prompt)

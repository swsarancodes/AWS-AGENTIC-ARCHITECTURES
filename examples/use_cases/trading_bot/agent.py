from patterns.base.agent_base import AgentBase

class TradingBot(AgentBase):
    def run(self, market_data):
        prompt = f"Analyze market data: {market_data}"
        return self.bedrock_client.invoke_model(prompt)

from patterns.base.agent_base import AgentBase
from patterns.base.bedrock_client import BedrockClient

class ReActAgent(AgentBase):
    """
    ReAct agent that performs reasoning and acting in an interleaved manner.
    """
    def __init__(self, config):
        super().__init__(config)
        self.bedrock = BedrockClient(region=config.get("region"))
        self.model_id = config.get("model_id", "anthropic.claude-3-sonnet-20240229-v1:0")
        self.max_steps = config.get("max_steps", 10)

    def run(self, input_data):
        steps = []
        for i in range(self.max_steps):
            thought = self._reason(input_data, steps)
            action = self._act(thought)
            steps.append({"thought": thought, "action": action})
            if self._is_done(action):
                break
        return steps

    def _reason(self, input_data, steps):
        prompt = f"Given input: {input_data}, and previous steps: {steps}, what should I think next?"
        return self.bedrock.invoke_model(self.model_id, prompt)

    def _act(self, thought):
        return f"Action based on: {thought}"

    def _is_done(self, action):
        return "done" in action.lower()

    def get_config(self):
        return self.config

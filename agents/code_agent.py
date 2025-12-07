from config import CODING_AGENT

from langchain_ollama import ChatOllama


class CodingAgent:

    def __init__(self, tools) -> None:
        self.agent = ChatOllama(
            model=CODING_AGENT,
            validate_model_on_init=True,
            temperature=0
        ).bind_tools(tools)

        self.systemPrompt = """You are a software engineer"""

    def invoke(self, state):
        result = self.agent.invoke(state["messages"][-1])
        return result



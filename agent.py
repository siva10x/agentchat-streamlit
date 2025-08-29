import yaml
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_core import CancellationToken
from autogen_ext.models.openai import OpenAIChatCompletionClient

import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


class Agent:
    def __init__(self) -> None:
        model_client = OpenAIChatCompletionClient(
            model="gpt-4o-mini",     # pick a model available to your key
            api_key=OPENAI_API_KEY
        )
        
        self.agent = AssistantAgent(
            name="assistant",
            model_client=model_client,
            system_message="You are a helpful AI assistant.",
        )

    async def chat(self, prompt: str) -> str:
        response = await self.agent.on_messages(
            [TextMessage(content=prompt, source="user")],
            CancellationToken(),
        )
        assert isinstance(response.chat_message, TextMessage)
        return response.chat_message.content
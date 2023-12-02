from autogen.agentchat import (
    Agent,
    AssistantAgent,
    UserProxyAgent,
)
from typing import Dict, List, Optional, Union
import os
from dotenv import load_dotenv


# https://github.com/PanoEvJ/Tiny_Agents/blob/main/src/backup/agentchat_groupchat.ipynb


class AgentSpawner:  # Group chat GroupChatSpawner class
    def __init__(self, llm_config: Dict[str, any], agents: List[str]):
        self.llm_config = llm_config

    def spawn(self) -> List[Agent]:
        pass

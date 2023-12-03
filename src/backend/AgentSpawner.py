from autogen.agentchat import (
    Agent,
    AssistantAgent,
    UserProxyAgent,
)
from typing import Dict, List, Optional, Union
import os
from dotenv import load_dotenv
import autogen

# https://github.com/PanoEvJ/Tiny_Agents/blob/main/src/backup/agentchat_groupchat.ipynb


class AgentSpawner:  # Group chat GroupChatSpawner class
    def __init__(self, name:List[str,any], system_message:List[str,any],human_input_mode:List[str,any], llm_config: Dict[str, any],agent_type:List[str,any]):
        self.name = name
        self.llm_config = llm_config
        self.system_message = system_message
        self.human_input_mode = human_input_mode
        self.llm_config = llm_config
        self.agent_type = agent_type

    def spawn(self) -> List[Agent]:
        agents = []
        for index, ag_type in enumerate(self.agent_type):
            if ag_type == 'assistant':
                agents.append(autogen.AssistantAgent(
                    name=self.name[index],
                    system_message=self.system_message[index],
                    # human_input_mode=self.human_input_mode[index],
                    llm_config=self.llm_config[index],
                    )
                )
            elif ag_type == 'userproxy':
                agents.append(autogen.UserProxyAgent(
                    name=self.name[index],
                    human_input_mode=self.human_input_mode[index],
                    system_message=self.system_message[index],
                    llm_config=self.llm_config[index],
                    )
                )
        return agents
        


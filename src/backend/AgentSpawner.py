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
load_dotenv()


class AgentSpawner:  # Group chat GroupChatSpawner class
    def __init__(
        self,
        name: List[str],
        system_message: List[str],
        human_input_mode: List[str],
        llm_config: Dict[str, any],
        agent_type: List[str],
    ):
        self.name = name
        self.llm_config = llm_config
        self.system_message = system_message
        self.human_input_mode = human_input_mode
        self.llm_config = llm_config
        self.agent_type = agent_type

    def spawn(self) -> List[Agent]:
        agents = []
        for index, ag_type in enumerate(self.agent_type):
            if ag_type == "assistant":
                agents.append(
                    autogen.AssistantAgent(
                        name=self.name[index],
                        system_message=self.system_message[index],
                        # human_input_mode=self.human_input_mode[index],
                        llm_config=self.llm_config,
                    )
                )
            elif ag_type == "userproxy":
                agents.append(
                    autogen.UserProxyAgent(
                        name=self.name[index],
                        human_input_mode=self.human_input_mode[index],
                        system_message=self.system_message[index],
                        llm_config=self.llm_config,
                    )
                )
        return agents


def combine_description_and_skills(
    data: Dict[str, Dict[str, any]], llm_config
) -> AgentSpawner:
    agent_type = []
    names = []
    system_message = []
    human_input_mode = []
    for key, values in data.items():
        agent_type.append(values["agent_type"])
        names.append(values["name"])
        human_input_mode.append(values["human_input_mode"])
        system_message.append(
            values["description"] + " with skillset in " + " ".join(values["skills"])
        )

    # You need to define llm_config according to your needs
    # llm_config = {}

    return AgentSpawner(
        name=names,
        system_message=system_message,
        human_input_mode=human_input_mode,
        llm_config=llm_config,
        agent_type=agent_type,
    )


json_data = {
    "1": {
        "name": "sales",
        "agent_type": "assistant",
        "description": "sales agents",
        "skills": ["sales", "customer service", "communication"],
        "human_input_mode": "TERMINATE",
    },
    "2": {
        "name": "marketing",
        "agent_type": "assistant",
        "description": "marketing agents",
        "skills": ["marketing", "communication"],
        "human_input_mode": "",
    },
    "3": {
        "name": "engineer",
        "agent_type": "assistant",
        "description": "engineers",
        "skills": ["python", "linux", "communication"],
        "human_input_mode": "",
    },
}
config_list_gpt4 = [
    {
        "model": "gpt-4",
        "api_key": os.getenv("OPENAI_API_KEY"),
        # "api_key": str(os.environ["OPENAI_API_KEY"]),
    },
    {
        "model": "gpt-4",
        "api_key": os.getenv("OPENAI_API_KEY"),
    },
]
llm_config = {"config_list": config_list_gpt4}
agent_spawner = combine_description_and_skills(json_data, llm_config)

all_agents = agent_spawner.spawn()
print(all_agents)

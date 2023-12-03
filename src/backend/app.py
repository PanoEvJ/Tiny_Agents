from autogen.agentchat import (
    Agent,
    GroupChat,
    GroupChatManager,
    AssistantAgent,
    UserProxyAgent,
)
import openai
from typing import Dict, List, Optional, Union
import os
from dotenv import load_dotenv

# from HumanResources import HumanResources
from AgentSelector import AgentSelector
from AgentSpawner import AgentSpawner
from GroupChatSpawner import GroupChatSpawner
from AgentSpawner import AgentSpawner, combine_description_and_skills
import HumanResources

openai.api_key = os.getenv("OPENAI_API_KEY")

CHAT_INITIATOR = "finance"

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


hr = HumanResources.HumanResources(chat_initiator="CHAT_INITIATOR")
all_available_agents = hr.select_agents()
print(all_available_agents)

task = "revenue in the east coast is falling and the competitor is doing great with their product."
selector = AgentSelector(task=task, available_agents=all_available_agents, n_agents=3)
selected_agents = selector.run_selection()
print(selected_agents)

# selected_agents = ["sales", "marketing", "engineer"]
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
agent_spawner = combine_description_and_skills(json_data, llm_config)
spawned_agents = agent_spawner.spawn()
print(spawned_agents)

messages = []
groupchat = GroupChatSpawner(
    agents=spawned_agents, llm_config=llm_config, messages=messages, max_round=10
)
manager = groupchat.spawn()

import autogen

chat_initiator = autogen.UserProxyAgent(
    name="Proxy",
    human_input_mode="TERMINATE",
    system_message="You are only initiating the chat. You are not participating in the chat.",
    llm_config=llm_config,
)

chat_initiator.initiate_chat(
    manager,
    message="I want to design an app to make me one million dollars in one month. Yes, your heard that right.",
)

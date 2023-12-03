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
from HumanResources import HumanResources
from AgentSelector import AgentSelector
from AgentSpawner import AgentSpawner
from GroupChatSpawner import GroupChatSpawner

openai.api_key = os.getenv("OPENAI_API_KEY")

CHAT_INITIATOR = "finance"

hr = HumanResources()
all_available_agents = hr.select_agents()
print(all_available_agents)

task = "revenue in the east coast is falling and the competitor is doing great with their product."
selector = AgentSelector(task=task, available_agents=all_available_agents, n_agents=3)
selected_agents = selector.run_selection()
print("*" * 10, selected_agents)

selected_agents = ["sales", "marketing", "engineer"]
agent_spawner = AgentSpawner(selected_agents, CHAT_INITIATOR)
agents = agent_spawner.spawn()
print(agents)

messages = []
llm_config = {"config_list": [{"model": "gpt-4"}], "seed": 42, "request_timeout": 600}
groupchat = GroupChatSpawner(
    agents=agents, llm_config=llm_config, messages=messages, max_round=10
)

chat_initiator.initiate_chat(
    manager,
    message="I want to design an app to make me one million dollars in one month. Yes, your heard that right.",
)

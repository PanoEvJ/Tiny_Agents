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

# load_dotenv()

hr = HumanResources()
all_available_agents = hr.select_agents()
print(all_available_agents)

task = "revenue in the east coast is falling and the competitor is doing great with their product."
selector = AgentSelector(task=task, available_agents=all_available_agents, n_agents=3)
selected_agents = selector.run_selection()
print("*" * 10, selected_agents)
selected_agents = []

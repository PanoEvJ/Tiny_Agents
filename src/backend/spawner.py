from autogen.agentchat import Agent, GroupChat, GroupChatManager, AssistantAgent
from typing import Dict, List, Optional, Union
import os
from dotenv import load_dotenv


# https://github.com/PanoEvJ/Tiny_Agents/blob/main/src/backup/agentchat_groupchat.ipynb


class Spawner: # Group chat spawner class
    """(In preview) A group chat class that contains the following data fields:
        - agents: a list of participating agents.
        - messages: a list of messages in the group chat.
        - max_round: the maximum number of rounds.
        - allow_repeat_speaker: whether to allow the same speaker to speak consecutively. Default is True.
        - speaker_selection_method: the method for selecting the next speaker. Default is "auto".
        - llm_config: to give to the GroupChatManager

        
        And returns:    the spawner should retrieve the memory of the chat history
    """
    

    # Use Groupchat object! 

    def __init__(
            self,
            agents: List[Agent],
            llm_config: Dict[str, any],
            messages: List[Dict],
            max_round: int = 10,
            speaker_selection_method: str = "auto",
            allow_repeat_speaker: bool = True
        ):    
        self.agents = agents
        self.messages = messages
        self.max_round = max_round
        self.speaker_selection_method = speaker_selection_method
        self.allow_repeat_speaker = allow_repeat_speaker
        self.llm_config = llm_config

    def spawn(self) -> GroupChatManager:
        """Docstring
        """
        groupchat = GroupChat(agents=self.agents, 
                  messages = self.messages, 
                  max_round = self.max_round,
                  speaker_selection_method = self.speaker_selection_method,
                  allow_repeat_speaker = self.allow_repeat_speaker)
        
        return GroupChatManager(groupchat = groupchat,
                                llm_config = self.llm_config)
    
    
    def retrieve_memory(self) -> list[str]:
        pass

if __name__ == "__main__":
    load_dotenv()
    
    config_list_gpt4 = [
    {
        "model": "gpt-3.5-turbo",
        "api_key": os.getenv("OPENAI_API_KEY"),
        # "api_key": str(os.environ["OPENAI_API_KEY"]),
    },
    {
        "model": "gpt-3.5-turbo",
        "api_key": os.getenv("OPENAI_API_KEY"),
    },    
]   
    llm_config = {"config_list": config_list_gpt4}
    print("loading dotenv", config_list_gpt4, llm_config)

    
    agents_sales = [
    AssistantAgent(
        name="Sales1",
        system_message="You are the team leader of the sales team, your team consists of Sales2 and Sales3. You can talk to the other team leaders: Marketing1, CustomerSupport1, ProductDevelopment1. Use 'NEXT: <agent_name>' to suggest the next speaker.",
        llm_config=llm_config,
    ),
    AssistantAgent(
        name="Sales2",
        system_message="You are team member Sales2, you are responsible for communication with ClientA.",
        llm_config=llm_config,
    ),
    AssistantAgent(
        name="Sales3",
        system_message="You are team member Sales3, you are responsible for communication with ClientB.",
        llm_config=llm_config,
    ),
]   
    agents_managers = [
    AssistantAgent(
        name="Manager1",
        system_message="You are the manager of the company, responsible of managing and coordinating the activities of all teams and departments within the company. You can talk to all team leaders: Sales1, Marketing1, CustomerSupport1, ProductDevelopment1. Use 'NEXT: <agent_name>' to suggest the next speaker.",
        llm_config=llm_config,
    ),
]
    
    messages = ['Everyone cooperate and and solve the various incoming tasks and client requests. Team Sales has Sales1, Sales2, Sales3. Team Marketing has Marketing1, Marketing2, Marketing3. Team ProductDevelopment has ProductDevelopment1, ProductDevelopment2, ProductDevelopment3. Team CustomerSupport has CustomerSupport1, CustomerSupport2, CustomerSupport3. Team Managers has Manager1. Only members of the same team can talk to one another. Only team leaders (names ending with 1) can talk amongst themselves. You must use "NEXT: Sales1" to suggest talking to Sales1 for example; You can suggest only one person, you cannot suggest yourself or the previous speaker; You can also not suggest anyone.'
    ]

    print("Agents are initiated:",agents_managers, agents_sales)
    spawnerr = Spawner(agents_sales,
            llm_config,
            messages)
    
    print("Spawner initiated!", spawnerr)
    agents_managers[0].initiate_chat(
    spawnerr.spawn(),
    message="ClientA, who recently purchased an e-bike from our company, has reported that after only a few weeks of regular use, the e-bike's battery began to malfunction. Please investigate and resolve the issue.",
)
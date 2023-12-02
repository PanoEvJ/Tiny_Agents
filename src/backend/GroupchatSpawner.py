from autogen.agent import Agent
from autogen.groupchat import GroupChat

# https://github.com/PanoEvJ/Tiny_Agents/blob/main/src/backup/agentchat_groupchat.ipynb


class GroupclassSpawner:
    """agents_to_use: List, number_of_message_exchanges: int = 10) → GroupChat:
    the spawner should retrieve the memory of the chat history
    """

    def __init__(self, agents: list[Agent], number_of_messages: int = 10):
        pass

    def retrieve_memory(self) -> list[str]:
        pass

    def spawn(self) -> GroupChat:
        pass

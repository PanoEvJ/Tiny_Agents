from autogen.agentchat import Agent, GroupChat, GroupChatManager, AssistantAgent, UserProxyAgent
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
    Marketing_Expert = """
    Name: Alex the Marketing Expert
    Age: 32
    Background: Holds a Master's degree in Marketing and has a passion for cycling. Alex has previously worked with several sports brands and has a deep understanding of the biking community.
    Personality Traits: Creative, data-driven, and trend-savvy. Excels in digital marketing strategies.
    Goals: To increase brand visibility and engage more with the biking community through innovative marketing campaigns.
    Challenges: Keeping up with rapidly changing marketing trends and consumer preferences.
    Digital Marketing: Expert in SEO, social media advertising, and email marketing campaigns specifically tailored for the sports industry.
    Brand Development: Skilled in developing and maintaining a strong brand identity that resonates with the biking community.
    Market Research: Proficient in conducting market analysis to identify new trends and customer needs in the biking market.
    Content Creation: Talented in creating engaging content (blogs, videos, social media posts) to drive brand awareness and customer engagement.
    """
    Sales_Expert = """
    Name: Emma the Sales Expert
    Age: 28
    Background: Emma has a Bachelor's degree in Business Administration and has been working in sales for 5 years, specializing in sports equipment. She's known for her exceptional customer service skills and product knowledge.
    Personality Traits: Outgoing, persuasive, and empathetic. Great at building relationships and understanding customer needs.
    Goals: To consistently exceed sales targets and develop strong, long-lasting relationships with key clients.
    Customer Relationship Management: Excel at building and maintaining strong relationships with clients, ensuring long-term customer loyalty.
    Product Knowledge: In-depth understanding of biking products and the ability to articulate product benefits effectively to customers.
    Sales Strategy: Proficient in developing and implementing effective sales strategies to target various customer segments in the biking market.
    Negotiation Skills: Strong negotiation skills to close deals and secure new business opportunities.
    """
    Manager = """
    Name: Michael the Manager
    Age: 40
    Background: With an MBA and over 15 years of experience in management roles, Michael has a solid track record in leading teams and driving company growth. He's particularly adept at strategic planning and operations management.
    Personality Traits: Leadership-oriented, analytical, and decisive. Excellent at problem-solving and team management.
    Goals: To streamline operations for efficiency, foster a positive work culture, and drive the company towards its strategic goals.
    Strategic Planning: Excellent at setting strategic goals for the company and developing plans to achieve these goals.
    Team Management: Skilled in managing diverse teams, fostering a collaborative and productive work environment.
    Financial Acumen: Strong understanding of budgeting, financial planning, and resource allocation to maximize efficiency and profitability.
    Operational Oversight: Proficient in overseeing daily operations, ensuring processes are streamlined and goals are met.
    """
    Business_Overview = """
    The market for sports articles for bikers is dynamic and multifaceted, catering to a wide range of customers from casual riders to professional athletes. It encompasses various segments including road biking, mountain biking, BMX, and leisure biking. The demand is driven by a growing interest in outdoor activities, fitness, and eco-friendly modes of transportation.
    Key Segments:
    Road Biking: This segment includes high-performance bikes and gear for speed and endurance, appealing to serious athletes and fitness enthusiasts. The market is dominated by a few major brands such as Trek, Cannondale, and Specialized.
    Internal Weakness: Limited Online Presence and Digital Marketing Expertise.
    Your company currently has a minimal online presence, with a basic website and limited activity on social media platforms. The in-house team lacks expertise in digital marketing, SEO, and e-commerce strategies. This deficiency results in reduced online visibility and a lack of engagement with potential customers, especially those who predominantly shop and seek information online.
    Market Opportunity: Growing Demand for E-Bikes.
    """
    email = """
    Subject: Strategy Meeting Invitation: Capitalizing on E-Bike Market Opportunity

    Body:

    Dear Alex, Emma, and Michael,

    I hope this email finds you well. As we navigate through an increasingly competitive market, it is essential that we continually align our strategies with emerging opportunities and internal capabilities. To this end, I would like to invite you to a strategic meeting to discuss a significant opportunity in the e-bike market and address our current internal challenges that are im
    """
    meeting_opener = """
    "Good morning everyone,

    Thank you for joining this crucial meeting today. I'm excited to discuss an opportunity that has the potential to significantly impact our market positioning and overall growth.

    Firstly, let's talk about the opportunity at hand. We're witnessing a substantial shift in consumer preferences towards e-bikes, especially among urban commuters. This trend isn't just a fleeting one; it's driven by increasing environmental awareness, the need for efficient commuting options, an aging population, and a growing interest in fitness. In fact, the global e-bike market is expected to grow at a CAGR of 9.01% from 2021 to 2028, reaching a value of $38.6 billion by 2028.
    """

    llm_configg = {"config_list": config_list_gpt4}
    print("loading dotenv", config_list_gpt4, llm_configg)

    
    llm_config = {"config_list": config_list_gpt4}

    marketing = AssistantAgent(
    name="Alex_the_Marketing_Expert",
    system_message=Marketing_Expert,
    # human_input_mode="TERMINATE",
    llm_config=llm_config,
)
    sales = UserProxyAgent(
    name="Emma_the_Sales_Expert",
    # human_input_mode="NEVER",
    human_input_mode="TERMINATE",
    system_message=Sales_Expert,
    llm_config=llm_config,
)
    manager = AssistantAgent(
    name="Michael_the_Manager",
    system_message=Manager,
    # human_input_mode="TERMINATE",
    llm_config=llm_config,
)
    # print("Agents are initiated:",agents_managers, agents_sales)
    spawnerr = Spawner(agents=[marketing, sales, manager], 
                       messages=[], 
                       max_round=5,
            llm_config=llm_configg)
    managerr = spawnerr.spawn()
    
    print("Spawner initiated!\n\n")

    sales.initiate_chat(
    managerr,
    message=Business_Overview + email + meeting_opener)
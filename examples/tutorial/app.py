import os
import autogen

# start logging
# autogen.ChatCompletion.start_logging()

config_list = [
    {
        "model": "gpt-3.5-turbo-16k",
        'api_key': os.environ['OPENAI_API_KEY'],
    }
]

llm_config = {
    "timeout": 600,
    "seed": 42,
    "config_list": config_list,
    "temperature": 0
}

assistant = autogen.AssistantAgent(
    name="CTO",
    llm_config=llm_config,
    system_message="Chief Technology Officer",
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content","").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "web"},
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been resolved at full satisfaction.
                    Otherwise, reply CONTINUE, or the reason why the task is not solved yet.""",
)

task="""
Give me a summary of this article: https://blog.perplexity.ai/blog/introducing-pplx-online-llms
"""

user_proxy.initiate_chat(
    assistant,
    message=task,
)

# print the chat log
print(autogen.ChatCompletion.logged_history)
autogen.ChatCompletion.print_usage_summary()

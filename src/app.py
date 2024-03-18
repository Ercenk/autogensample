from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

config_list = [
    {
        "model": "ollama/mistral",
        "base_url": "http://localhost:8040/v1",
        "api_type": "openai",
        "api_key": "NOTNEEDED"
    }
]

assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})

user_proxy = UserProxyAgent(
    "user_proxy", 
    code_execution_config=
        {
            "work_dir": "coding", 
            "use_docker": True}) # IMPORTANT: set to True to run code in docker, recommended
user_proxy.initiate_chat(
    assistant, 
    message="Plot a chart of NVDA and TESLA stock price change YTD.")

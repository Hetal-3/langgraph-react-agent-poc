import os
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()

@tool
def triple(num:float)->float:
    """
    param num: a number to triple
    return:  the triple of that number
    """
    return float(num)*3

tools=[TavilySearch(max_results=1),triple]

llm = ChatOpenAI(
    model="nvidia/nemotron-3.5-lightning:free",
    temperature=0,
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPEN_ROUTER_API_KEY"),
).bind_tools(tools)
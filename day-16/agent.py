import yaml
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_react_agent, AgentExecutor

from tools.knowledge_base import search_docs
from tools.calculator import calculate

def build_agent():
    with open("prompts/agent.yaml") as f:
        prompt_data = yaml.safe_load(f)
    
    prompt = ChatPromptTemplate.from_template(
        prompt_data['template']
    )
    
    llm = ChatOpenAI(
        model='gpt-4.1',
        temperature=0.0
    )
    
    tools= [search_docs, calculate]
    
    agent = create_react_agent(
        llm = llm,
        tools = tools,
        prompt = prompt
    )
    
    return AgentExecutor(
        agent=agent,
        tools= tools,
        max_iteration= 4,
        verbose = True
    )
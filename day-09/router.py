import yaml
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from chains.cheap_chain import build_cheap_chain
from chains.mid_chain import build_mid_chain
from chains.expensive_chain import build_expensive_chain

def build_router():
    with open("prompts/analyzer.yaml") as f:
        prompt_data = yaml.safe_load(f)
        
    prompt = ChatPromptTemplate.from_template(
        prompt_data['template']
    )
    
    analyzer_llm = ChatOpenAI(
        model='gpt-4.1-mini',
        temperature= 0.0
    )
    
    analyzer_chain = prompt | analyzer_llm
    
    cheap = build_cheap_chain()
    mid = build_mid_chain()
    expensive = build_expensive_chain()
    
    def route(input_text: str):
        category = analyzer_chain.invoke(
            {'input': input_text}
        ).content.strip().lower()
        
        if category == 'simple':
            return cheap.invoke(input_text)
        elif category == 'medium':
            return mid.invoke(input_text)
        else:
            return expensive.invoke(input_text)
    
    return route

# this is correct
# Routing is deterministic
# Policy is centralized
# Models are swappable
# Costs are controllable
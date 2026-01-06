from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

def build_heavy_chain():
    prompt = ChatPromptTemplate.from_template(
        "Analyse the following input deeply:\n{input}"
    )
    
    llm = ChatOpenAI(
        model='gpt-4.1',
        temperature=0.0
    )
    
    return prompt | llm
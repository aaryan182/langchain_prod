from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

def build_chain():
    prompt = ChatPromptTemplate.from_template(
        "Process this input:\n{input}"
    )
    
    llm = ChatOpenAI(
        model='gpt-4.1',
        temperature=0.0
    )
    
    return prompt | llm


# Critical point:

# Chains live in shared code not API or worker folders.
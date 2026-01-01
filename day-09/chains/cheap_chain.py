from langchain_openai import ChatOpenAI

def build_cheap_chain():
    llm = ChatOpenAI(
        model = 'gpt-4.1-mini',
        temperature= 0.0,
        timeout=15
    )
    
    return llm
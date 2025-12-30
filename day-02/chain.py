from langchain_openai import ChatOpenAI
from prompts import build_prompt

def build_chain():
    """
    this function returns a runnable.
    Runnables are FIRST-CLASS objects in LangChain.
    """
    prompt = build_prompt()
    
    llm = ChatOpenAI(
        model = 'gpt-4.1-mini',
        temperature = 0.0,  # Determinism > creativity in prod
        timeout= 30
    )
    
    # LCEL composition
    chain = prompt | llm
    
    return chain


# Important production insights
# temperature=0 by default in real systems
# Timeouts are explicit
# Chain is reusable and testable
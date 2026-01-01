from langchain_openai import ChatOpenAI

def build_expensive_chain():
    llm = ChatOpenAI(
        model="gpt-4.1",
        temperature=0.2,
        timeout=60
    )

    return llm
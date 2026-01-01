from langchain_openai import ChatOpenAI

def build_mid_chain():
    llm = ChatOpenAI(
        model="gpt-4.1",
        temperature=0.0,
        timeout=30
    )

    return llm
from langchain_core.prompts import ChatPromptTemplate

SYSTEM_PROMPT = """
You are a senior software engineer.
You answer precisely, concisely and without speculation.
If information is insufficient you say so explicitly.
"""

def build_prompt():
    """
    PromptTemplate is an INTERFACE.
    Teat it like an API contract.
    """
    return ChatPromptTemplate.from_message(
        [
            ("system", SYSTEM_PROMPT),
            ("user", "{question}")
        ]
    )
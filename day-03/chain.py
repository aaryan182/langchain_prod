from langchain_openai import ChatOpenAI
from prompt_loader import load_prompt

def build_chain(prompt_path: str):
    """
    Prompt is injected.
    This allows:
    - A/B testing
    - Rollbacks
    - Version pinning
    """
    prompt = load_prompt(prompt_path)

    llm = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0.0,
        timeout=30
    )

    return prompt | llm
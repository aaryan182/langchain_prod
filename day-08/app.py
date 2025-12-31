# app.py
from dotenv import load_dotenv
load_dotenv()

from chains.conversational_chain import build_conversational_chain
from memory.short_term import build_short_term_memory
from memory.long_term import build_long_term_memory

def main():
    short_term = build_short_term_memory()
    long_term = build_long_term_memory()

    chain = build_conversational_chain(
        "prompts/assistant.yaml",
        short_term,
        long_term
    )

    print(chain.invoke({"input": "What should I focus on for AI interviews?"}).content)
    print(chain.invoke({"input": "Does this align with my background?"}).content)

if __name__ == "__main__":
    main()

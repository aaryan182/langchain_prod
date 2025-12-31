from chain import build_chain

RESUME_TEXT = """
Software engineer with experience in Python and FastAPI.
"""

def main():
    chain = build_chain()

    result = chain.invoke(
        {"resume": RESUME_TEXT}
    )

    print("Final structured output:")
    print(result)

if __name__ == "__main__":
    main()
    
    

# Transient failures → retried
# Persistent failures → fallback model
# Output still validated
# System never crashes silently
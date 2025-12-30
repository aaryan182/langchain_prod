from chain import build_chain

def main():
    chain = build_chain()
    
    response = chain.invoke(
        {"question": "Why are LLMs considered unreliable in production systems?"}
    )
    
    print(response.content)

if __name__ == "__main__":
    main()
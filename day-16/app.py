from dotenv import load_dotenv
load_dotenv()

from agent import build_agent

def main():
    agent = build_agent()
    
    print(agent.invoke({"input": "What is the API rate limit?"}))
    print(agent.invoke({"input": "If I make 20 requests per minute for 5 minutes, how many requests total?"}))

if __name__ == "__main__":
    main()
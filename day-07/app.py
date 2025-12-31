from dotenv import load_dotenv
load_dotenv()

from agent import build_agent

def main():
    agent = build_agent()

    print(agent.invoke({"input": "Get resume for candidate 123"}))
    print(agent.invoke({"input": "Normalize skill fast api"}))
    print(agent.invoke({"input": "Tell me a joke"}))

if __name__ == "__main__":
    main()
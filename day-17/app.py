from dotenv import load_dotenv
load_dotenv()

from agent import build_decision_agent
from decision_gate import build_decision_gate

def main():
    agent = build_decision_agent()
    gate = build_decision_gate()

    user_input = "Close user account immediately"

    decision = agent.invoke({"input": user_input})
    assessment = gate(decision)

    print("Proposed Action:", decision)
    print("Risk Assessment:", assessment)

    if assessment.requires_human:
        print(" Escalated for human approval")
    else:
        print(" Auto approved")

if __name__ == "__main__":
    main()
from dotenv import load_dotenv
load_dotenv()

from evaluator import build_evaluator
from test_cases import TEST_CASES

# Day 13 RAG system here
# from rag_system import rag

def fake_rag_answer(question: str) -> str:
    """
    Replace this with your actual RAG system call.
    """
    if "OAuth" in question:
        return "I don’t have enough information to answer that."
    if "rate limit" in question:
        return "The API rate limit is 100 requests per minute."
    if "password" in question:
        return "Password resets expire after 15 minutes."
    return "Default Answer"

def main():
    evaluator = build_evaluator()

    for case in TEST_CASES:
        answer = fake_rag_answer(case["question"])

        result = evaluator.invoke({
            "question": case["question"],
            "answer": answer,
            "expected_behavior": case["expected_behavior"]
        })

        print("Question:", case["question"])
        print("Evaluation:", result)
        print("-" * 50)

if __name__ == "__main__":
    main()
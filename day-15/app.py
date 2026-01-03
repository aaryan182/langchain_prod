from dotenv import load_dotenv
load_dotenv()

from rag_chain import rag_answer

def main():
    answer = rag_answer("What is the API rate limit?")
    print("Final Answer:", answer)

if __name__ == "__main__":
    main()
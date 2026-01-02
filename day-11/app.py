from dotenv import load_dotenv
load_dotenv()

from ingest import ingest_documents
from rag_chain import build_rag_chain

def main():
    vectorstore = ingest_documents("data/handbook.txt")
    rag = build_rag_chain(vectorstore)

    print(rag.invoke({"question": "What is the API rate limit?"}).content)
    print(rag.invoke({"question": "How long do password resets last?"}).content)
    print(rag.invoke({"question": "Do you support OAuth?"}).content)

if __name__ == "__main__":
    main()
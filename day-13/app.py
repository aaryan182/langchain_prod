from dotenv import load_dotenv
load_dotenv()

from ingest import ingest_documents
from retriever import build_advanced_retriever
from rag_chain import build_rag_chain

def main():
    vectorstore = ingest_documents("data/handbook.txt")
    retriever = build_advanced_retriever(vectorstore)
    rag = build_rag_chain(retriever)

    print(rag.invoke({"question": "What is the API rate limit?"}))
    print(rag.invoke({"question": "How long do password resets last?"}))
    print(rag.invoke({"question": "Do you support OAuth?"}))

if __name__ == "__main__":
    main()
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def build_vectorstore(texts: list[str]):
    embeddings = OpenAIEmbeddings()
    return FAISS.from_texts(texts, embedding=embeddings)
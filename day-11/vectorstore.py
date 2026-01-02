from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def build_vectorstore(texts: list[str]):
    embeddings = OpenAIEmbeddings()
    
    return FAISS.from_texts(
        texts= texts,
        embeddings= embeddings
    )
    
# Why this is correct
# Vector store is isolated
# Swappable later (Pinecone, Weaviate, Milvus)
# No LLM logic here
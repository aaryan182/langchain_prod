from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def build_long_term_memory():
    """
    Long term memory:
    - Semantic facts
    - Persistent
    - Retrieved selectively
    """
    embeddings = OpenAIEmbeddings()
    
    # In production: Pinecone
    vector_store = FAISS.from_texts(
        texts= [
            "User prefers python over javascript",
            "User is preparing for AI engineer intervies"
        ],
        embedding = embeddings
    )
    
    return vector_store
    
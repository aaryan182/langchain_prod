from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_openai import ChatOpenAI

def build_advanced_retriever(vectorstore):
    """
    Builds a high-precision retriever using:
    - Vector recall
    - LLM-based compression
    """

    base_retriever = vectorstore.as_retriever(
        search_kwargs={"k": 8}
    )

    compressor_llm = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0.0
    )

    compressor = LLMChainExtractor.from_llm(
        compressor_llm
    )

    return ContextualCompressionRetriever(
        base_retriever=base_retriever,
        base_compressor=compressor
    )
    
# this works

# Vector DB gives high recall
# Compressor removes irrelevant sentences
# Context becomes short + precise
# Token usage drops significantly
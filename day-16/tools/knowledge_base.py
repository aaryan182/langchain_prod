from langchain_core.tools import tool

@tool
def search_docs(query: str) -> str:
    """
    Search internal knowledge base.
    Read-only, safe tool.
    """
    
    docs = {
        "rate limit": "API rate limit is 100 requests per minute",
        "password reset": "Password reset expire after 15 minutes"
    }
    
    for key, value in docs.items():
        if key in query.lower():
            return value
    
    return "No relevant documents found."
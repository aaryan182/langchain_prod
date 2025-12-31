from langchain_core.tools import tool

@tool
def normalize_skill(skill: str) -> str:
    """
    Normalize skill names to internal taxonomy.
    """
    mapping = {
        "fast api": "FASTAPI",
        "postgres": "PostgreSQL",
        "js": "Javascript"
    }
    
    return mapping.get(skill.lower() , skill)
from langchain_core.tools import tool

@tool
def fetch_resume(candidate_id: str) -> str:
    """
    Fetch resume text for a candidate.
    Only returns data from internal storage.
    """
    fake_db = {
        "123": "Software Engineer with 2 years of experience in Python and FastAPI",
        "456": "Frontend engineer skilled in react and typescript"
    }
    
    return fake_db.get(candidate_id, "Resume not found")
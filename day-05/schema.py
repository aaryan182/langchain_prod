from pydantic import BaseModel, Field
from typing import List, Optional

class ResumeExtraction(BaseModel):
    name: Optional[str]
    years_of_experience: Optional[int]
    skills: List[str]
    seniority: str
    summary: str
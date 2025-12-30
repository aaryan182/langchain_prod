from pydantic import BaseModel, Field
from typing import List, Optional

class ResumeExtraction(BaseModel):
    """
    This schema is a HARD CONTRACT.
    If the LLM violates it we retry or fail.
    """
    
    name: Optional[str] = Field(
        description="Candidate full name if explicitly mentioned else null"
    )
    
    years_of_experience: Optional[int] = Field(
        description="Total years of professional experience if specified"
    )
    
    skills: List[str] = Field(
        description="List of explicitly mentioned technical skills"
    )
    
    seniority: str = Field(
        description="One of: junior, mid, senior, unknown"
    )
    
    summary: str = Field(
        description="Concise factual professional summary"
    )
    
    
# Why this matters

# Types are explicit
# Optional vs required is intentional
# Descriptions guide the model
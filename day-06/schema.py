from pydantic import BaseModel
from typing import List, Optional

class ClassificationResult(BaseModel):
    document_type: str
    confidence: float
    
class ExtractionResult(BaseModel):
    name: Optional[str]
    skills: List[str]
    years_of_experience: Optional[str]
    
class FinalResult(BaseModel):
    classification: ClassificationResult
    extraction: ExtractionResult
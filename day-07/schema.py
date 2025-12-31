from pydantic import BaseModel
from typing import Optional

class Decision(BaseModel):
    action: str
    candidate_id: Optional[str]
    skill: Optional[str]
    
    
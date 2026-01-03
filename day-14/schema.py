from pydantic import BaseModel, Field

class EvaluationResult(BaseModel):
    score: float = Field(
        description="Overall quality score between 0.0 and 1.0"
    )
    grounded: bool = Field(
        description="Is the answer grounded in provided context"
    )
    abstained_correctly: bool = Field(
        description="Did the system abstain when information was missing"
    )
    notes: str = Field(
        description="Brief explanation of the evaluation decision"
    )
    
    
from pydantic import BaseModel, Field

class RAGResponse(BaseModel):
    answer: str = Field(
        description="Final answer or abstention message"
    )
    confidence: float = Field(
        description="Confidence score between 0.0 and 1.0"
    )
    grounded: bool = Field(
        description="Whether the answer is supported by retrieved documents"
    )
    
    
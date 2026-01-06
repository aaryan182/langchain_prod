from pydantic import BaseModel, Field

class AgentDecision(BaseModel):
    action: str = Field(
        description="Proposed action"
    )
    rationale: str = Field(
        description="Why the agent proposes this action"
    )
    
class RiskAssessment(BaseModel):
    confidence: float = Field(
        description="Confidence score between 0.0 and 1.0"
    )
    risk_level: str = Field(
        description="low, medium or high"
    )
    requires_human: bool = Field(
        description="Whether human approval is requried"
    )
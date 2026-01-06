import yaml
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from schema import RiskAssessment

CONFIDENCE_THRESHOLD = 0.7

def build_decision_gate():
    parser = PydanticOutputParser(
        pydantic_object=RiskAssessment
    )

    with open("prompts/risk.yaml") as f:
        prompt_data = yaml.safe_load(f)

    prompt = ChatPromptTemplate.from_template(
        prompt_data["template"]
    ).partial(
        format_instructions=parser.get_format_instructions()
    )

    llm = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0.0
    )

    def evaluate(decision):
        assessment = (prompt | llm | parser).invoke({
            "action": decision.action,
            "rationale": decision.rationale
        })

        # Deterministic gate
        if assessment.confidence < CONFIDENCE_THRESHOLD:
            assessment.requires_human = True

        return assessment

    return evaluate

# This gate:
# Is explicit
# Is logged/auditable
# Does not rely on “gut feeling”
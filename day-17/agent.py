import yaml
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from schema import AgentDecision

def build_decision_agent():
    parser = PydanticOutputParser(
        pydantic_object=AgentDecision
    )

    with open("prompts/task.yaml") as f:
        prompt_data = yaml.safe_load(f)

    prompt = ChatPromptTemplate.from_template(
        prompt_data["template"]
    )

    llm = ChatOpenAI(
        model="gpt-4.1",
        temperature=0.0
    )

    return prompt | llm | parser


# Agent proposes actions never executes them.
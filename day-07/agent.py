from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnableLambda
from schema import Decision
import yaml

from tools.resume_store import fetch_resume
from tools.skill_lookup import normalize_skill

def build_agent():
    parser = PydanticOutputParser(pydantic_object=Decision)

    with open("prompts/decision.yaml") as f:
        prompt_data = yaml.safe_load(f)

    prompt = ChatPromptTemplate.from_template(
        prompt_data["template"]
    )

    llm = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0.0
    )

    decision_chain = prompt | llm | parser

    def executor(decision: Decision):
        if decision.action == "fetch_resume":
            return fetch_resume.invoke(decision.candidate_id)
        elif decision.action == "normalize_skill":
            return normalize_skill.invoke(decision.skill)
        else:
            return "No action required."

    return decision_chain | RunnableLambda(executor)


# Why this is production grade
# LLM never executes tools directly
# Tool execution is explicit
# Schema guarantees intent clarity
import yaml
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from schema import EvaluationResult

def build_evaluator():
    parser = PydanticOutputParser(
        pydantic_object = EvaluationResult
    )
    
    with open("prompts/eval.yaml") as f:
        prompt_data = yaml.safe_load(f)
        
    prompt = ChatPromptTemplate.from_template(
        prompt_data['template']
    ).partial(
        format_instructions = parser.get_format_instructions()
    )
    
    llm = ChatOpenAI(
        model= 'gpt-4.1-mini',
        temperature= 0.0
    )
    
    return prompt | llm | parser
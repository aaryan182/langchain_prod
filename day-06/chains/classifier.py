import yaml
from langchain_openai import ChatOpenAI
from langchain_output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from schema import ClassificationResult

def build_classifier():
    parser = PydanticOutputParser(
        pydantic_object= ClassificationResult
    )
    
    with open("prompts/classify.yaml") as f:
        prompt_data = yaml.safe_load(f)
        
    prompt = ChatPromptTemplate.from_template(
        prompt_data['template']
    ).partial(
        format_instructions = parser.get_format_instructions()
    )
    
    llm = ChatOpenAI(
        model= 'gpt-4.1-mini',
        temperature=0.0
    )
    
    return prompt | llm | parser
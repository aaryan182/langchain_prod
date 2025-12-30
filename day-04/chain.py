from langchain_openai import ChatOpenAI
from langchain_output_parsers import PydanticOutputParser
from langchain_core.concepts import ChatPromptTemplate
from schema import ResumeExtraction
import yaml

def build_chain():
    # Output parser enforces schema
    parser = PydanticOutputParser(
        pydantic_object = ResumeExtraction
    )
    
    # Load prompt
    with open("prompts/resume_extraction.yaml", "r") as f:
        prompt_data = yaml.safe_load(f)
    
    prompt = ChatPromptTemplate.from_template(
        prompt_data['template']
    ).partial(
        format_instructions = parser.get_format_instructions()
    )
    
    llm = ChatOpenAI(
        model = 'gpt-4.1-mini',
        temperature = 0.0,
        timeout = 30
    )
    
    # LCEL prompt -> llm -> parser
    chain = prompt | llm | parser
    
    return chain

# important here

# Parser is firstclass
# Prompt depends on parser not the other way around
# Chain output is now a typed Python object

import yaml
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from schema import ResumeExtraction
from resilience import with_retry, fallback_llm


def build_chain():
    parser = PydanticOutputParser(
        pydantic_object= ResumeExtraction
    )
    
    with open("prompts/resume_extraction.yaml", "r") as f:
        prompt_data = yaml.safe_load(f)
    
    prompt = ChatPromptTemplate.from_template(
        prompt_data['template']
    ).partial(
        format_instructions = parser.get_format_instructions()
    )
    
    primary_llm = ChatOpenAI(
        model= 'gpt-4.1',
        temperature= 0.0,
        timeout= 30
    )
    
    primary_chain = prompt | primary_llm | parser
    
    # adding retry logic
    resilient_primary = with_retry(primary_chain)
    
    # Fallback chain (same prompt + schema, different model)
    fallback_chain = prompt | fallback_llm() | parser
    
     # Final chain with fallback
    def safe_invoke(input_data):
        try:
            return resilient_primary.invoke(input_data)
        except Exception as e:
            print("Primary chain failed, using fallback:", str(e))
            return fallback_chain.invoke(input_data)

    return RunnableLambda(safe_invoke)

# Senior insights
# Retry ≠ fallback
# Fallback ≠ silence
# Schema stays enforced even in fallback
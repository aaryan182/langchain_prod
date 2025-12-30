import yaml
from langchain_core.prompts import ChatPromptTemplate

def load_prompt(path:str) -> ChatPromptTemplate:
    """
    Loads prompt templates from disk.
    
    This enforces:
    - Prompt externalization
    - Version control
    - Separation from code
    """
    with open(path, "r") as f:
        data = yaml.safe_load(f)
        
    template = data['template']
    
    return ChatPromptTemplate.from_template(template)
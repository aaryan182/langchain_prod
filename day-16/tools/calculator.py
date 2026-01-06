from langchain_core.tools import tool

@tool
def calculate(expression: str) -> str:
    """
    Perform basic arithmetic.
    """
    try: 
        return str(eval(expression))
    except Exception:
        return "Invalid expression"
    
    
# Note: In  real systems never use eval 
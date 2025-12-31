from langchain_core.runnables import RunnableRetry, RunnableLambda
from langchain_openai import ChatOpenAI

def with_retry(chain):
    """
    Adds retry logic for transient failures:
    - Timeouts
    - Rate Limits
    - Temporary parsing issues
    """
    return RunnableRetry(
        chain,
        max_attempts = 3,
        wait_exponential_jitter= True
    )
    
def fallback_llm():
    """
    Fallback model:
    - cheaper
    - Faster
    - Less capable but better than failure
    """
    return ChatOpenAI(
        model= 'gpt-4.1-mini',
        temperature= 0.0,
        timeout= 20
    )
    
# Why this matters

# Retry logic is explicit
# Fallback strategy is intentional
# No silent infinite loops
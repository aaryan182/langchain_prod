from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
import yaml

def build_conversational_chain(prompt_path, short_term_memory, 
                               long_term_memory):
    with open(prompt_path) as f:
        prompt_data = yaml.safe_load(f)
    
    prompt = ChatPromptTemplate.from_template(prompt_data['template'])
    
    llm = ChatOpenAI(
        model='gpt-4.1-mini',
        temperature= 0.0
    )
    
    def retrieve_context(input_text):
        docs= long_term_memory.similarity_search(input_text, k=2)
        return "\n".join([d.page_content for d in docs])
    
    def enrich_inputs(inputs):
        return {
            "input": inputs["input"],
            "chat_history": short_term_memory.load_memory_variables({})["chat_history"],
            "context": retrieve_context(inputs["input"])
        }

    chain = (
        RunnableLambda(enrich_inputs) | prompt | llm
    )

    return chain


# important here
# Memory is retrieved, not appended blindly
# Long-term memory is queried, not dumped
# Short-term memory stays bounded
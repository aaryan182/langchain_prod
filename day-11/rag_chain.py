import yaml
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda

def build_rag_chain(vectorstore):
    with open("prompts/rag_answer.yaml") as f:
        prompt_data = yaml.safe_load(f)
        
    prompt = ChatPromptTemplate.from_template(
        prompt_data['template']
    )
    
    llm = ChatOpenAI(
        model= 'gpt-4.1-mini',
        temperature = 0.0
    )
    
    def retrieve(inputs):
        docs = vectorstore.similarity_search(
            inputs['question'],
            k=2
        )
        return {
            'question': inputs['question'],
            'context': '\n'.join(d.page_content for d in docs)
        }
    
    return RunnableLambda(retrieve) | prompt | llm
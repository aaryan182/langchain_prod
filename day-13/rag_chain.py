import yaml 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from confidence_chain import build_confidence_chain

CONFIDENCE_THRESHOLD = 0.65

def build_rag_chain(retriever):
    with open("prompts/rag_answer.yaml") as f:
        prompt_data = yaml.safe_load(f)
        
    answer_prompt = ChatPromptTemplate.from_template(
        prompt_data['template']
    )
    
    llm = ChatOpenAI(
        model = 'gpt-4.1-mini',
        temperature = 0.0
    )
    
    confidence_chain = build_confidence_chain()
    
    def generate(inputs):
        docs = retriever.get_relevant_documents(
            inputs['question']
        )
        
        context = "\n".join(d.page_content for d in docs)
        
        answer = (answer_prompt | llm).invoke({
            "context": context,
            "question": inputs['question']
        }).content
        
        confidence_result = confidence_chain.invoke({
            "question": inputs['question'],
            "context": context,
            "answer": answer
        })
        
        if confidence_result.confidence < CONFIDENCE_THRESHOLD:
            return {
                "answer": "I don’t have enough information to answer that.",
                "confidence": confidence_result.confidence,
                "grounded": False
            }

        return confidence_result

    return RunnableLambda(generate)
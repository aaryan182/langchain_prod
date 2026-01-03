from observability.logger import log_event
from observability.tracer import trace_span

def rag_answer(question: str):
    with trace_span("rag_request", {"question": question}) as trace_id:
        # Simulated retrieval
        retrieved_docs = [
            "API rate limit is 100 requests per minute."
        ]

        log_event(
            "retrieval",
            {
                "trace_id": trace_id,
                "documents": retrieved_docs
            }
        )

        # Simulated model call
        answer = "The API rate limit is 100 requests per minute."

        log_event(
            "llm_response",
            {
                "trace_id": trace_id,
                "model": "gpt-4.1",
                "answer": answer,
                "confidence": 0.82,
                "estimated_cost_usd": 0.0021
            }
        )

        return answer
    
# Important:
# Retrieval logged
# Model metadata logged
# Confidence logged
# Cost estimated (rough)
from fastapi import FastAPI
import uuid


from queue import enqueue
from storage import get_result

app = FastAPI()

@app.post("/jobs")
def create_job(payload: dict):
    job_id = str(uuid.uuid4())
    
    enqueue({
        "job_id": job_id,
        "input": payload["input"]
    })

    return {
        "job_id": job_id,
        "status": "queued"
    }

@app.get("/jobs/{job_id}")
def get_job(job_id: str):
    result = get_result(job_id)

    if result is None:
        return {"status": "processing"}

    return {
        "status": "completed",
        "result": result
    }
    
# Why this is correct
# API returns immediately
# No LLM blocking
# Client controls polling
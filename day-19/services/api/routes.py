import uuid
from fastapi import FastAPI
from shared.queue import enqueue
from shared.storage import get

router = APIRouter()

@router.post("/jobs")
def create_job(payload: dict):
    job_id = str(uuid.uuid4())
    
    enqueue({
        "job_id": job_id,
        "input": payload['input']
    })
    
    return {"job_id": job_id, "status": "queued"}

@router.get("/jobs/{job_id}")
def get_job(job_id: str):
    result = get(job_id)
    if result is None:
        return {"status": 'processing'}
    return {"status": "completed", "result": result}


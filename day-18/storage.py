import uuid

_RESULTS = {}

def save_result(job_id: str, result: str):
    _RESULTS[job_id] = result

def get_result(job_id: str):
    return _RESULTS.get(job_id)
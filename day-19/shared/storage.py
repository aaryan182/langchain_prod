_RESULTS = {}

def save(job_id: str, result: str):
    _RESULTS[job_id] = result
    
def get(job_id: str):
    return _RESULTS.get(job_id)
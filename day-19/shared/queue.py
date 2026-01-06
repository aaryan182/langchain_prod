import queue

_job_queue = queue.Queue()

def enqueue(job: dict):
    _job_queue.put(job)

def dequeue():
    return _job_queue.get()

# In production: redis, sqs
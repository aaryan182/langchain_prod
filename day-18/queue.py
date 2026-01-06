import queue

job_queue = queue.Queue()

def enqueue(job: dict): 
    job_queue.put(job)

def dequeue():
    return job_queue.get()

# In production: redis, sqs, kafka
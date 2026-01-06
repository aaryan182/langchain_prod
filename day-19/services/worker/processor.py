from shared.queue import dequeue
from shared.storage import save
from shared.chains import build_chain

async def process_jobs():
    chain = build_chain()

    while True:
        job = dequeue()
        result = await chain.ainvoke(
            {"input": job["input"]}
        )
        save(job["job_id"], result.content)
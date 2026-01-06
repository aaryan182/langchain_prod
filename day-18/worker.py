import asyncio

from queue import dequeue
from storage import save_result
from chains.heavy_chain import build_heavy_chain

async def worker_loop():
    chain = build_heavy_chain()
    
    while True:
        job = dequeue()
        job_id = job['job_id']
        input_text = job['input']
        
        # async LLM execution
        response = await chain.ainvoke(
            {"input": input_text}
        )
        
        save_result(job_id, response.content)

async def main():
    await worker_loop()
    
if __name__ == "__main__":
    asyncio.run(main())
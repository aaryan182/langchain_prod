import asyncio
from services.worker.processor import process_jobs

if __name__ == "__main__":
    asyncio.run(process_jobs())
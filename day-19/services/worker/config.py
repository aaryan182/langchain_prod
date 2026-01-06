import os

class Settings:
    SERVICE_NAME = "llm-worker"
    ENV = os.getenv("ENV", "local")

    # Worker tuning
    MAX_CONCURRENCY = int(os.getenv("WORKER_MAX_CONCURRENCY", "1"))
    POLL_INTERVAL_SEC = float(os.getenv("WORKER_POLL_INTERVAL_SEC", "0.1"))

settings = Settings()
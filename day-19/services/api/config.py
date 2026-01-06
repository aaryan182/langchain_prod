import os

class Settings: 
    SERVICE_NAME = "llm-api"
    ENV = os.getenv("ENV", "local")

settings = Settings()
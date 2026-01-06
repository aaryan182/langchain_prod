from fastapi import FastAPI
from services.api.routes import router

app = FastAPI(title="LLM API Service")
app.include_router(router)
from fastapi import FastAPI
from app.api.router import api_router

app = FastAPI(
    title="FARO Quant System",
    version="1.0.0"
)

app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "FARO Quant System V46 funcionando"}

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
@app.head("/")
async def root():
    return {"message": "FARO Quant System V46 funcionando"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}

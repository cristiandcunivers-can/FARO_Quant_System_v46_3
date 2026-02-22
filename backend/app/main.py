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

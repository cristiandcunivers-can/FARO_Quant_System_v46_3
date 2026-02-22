# main.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
from app.engine import engine_v46p_brain

app = FastAPI(title="FARO Quant System V46.3")

# Health check
@app.get("/health")
async def health_check():
    return JSONResponse(content={"status": "ok"})

# Root
@app.get("/")
async def root():
    return JSONResponse(content={"message": "FARO Quant System V46.3 funcionando"})

# Motor
@app.post("/run-engine")
async def run_engine(data: dict):
    try:
        df = pd.DataFrame(data.get("df"))
        portfolio_dict = data.get("portfolio", {})
        result = engine_v46p_brain(df, portfolio_dict)
        return JSONResponse(content=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

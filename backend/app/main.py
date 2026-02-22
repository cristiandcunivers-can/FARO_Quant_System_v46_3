# app/main.py

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
from app.engine import engine_v46p_brain

# ==========================================
# Instancia única de FastAPI
# ==========================================
app = FastAPI(title="FARO Quant System V46.3")

# ==========================================
# Health check simple
# ==========================================
@app.get("/health")
async def health_check():
    """
    Ruta de verificación de estado.
    Retorna 'ok' si el servicio está activo.
    """
    return JSONResponse(content={"status": "ok"})

# ==========================================
# Ruta principal
# ==========================================
@app.get("/")
async def root():
    """
    Ruta principal del sistema.
    """
    return JSONResponse(content={"message": "FARO Quant System V46.3 funcionando"})

# ==========================================
# Ruta Motor Cuantitativo
# ==========================================
@app.post("/run-engine")
async def run_engine(data: dict):
    """
    Ejecuta el motor cuantitativo con datos enviados en JSON.
    data debe contener:
    - df: lista de listas (simulando DataFrame)
    - portfolio: diccionario de pesos
    """
    try:
        df = pd.DataFrame(data.get("df"))
        portfolio_dict = data.get("portfolio", {})
        result = engine_v46p_brain(df, portfolio_dict)
        return JSONResponse(content=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

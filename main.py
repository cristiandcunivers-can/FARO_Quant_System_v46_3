import pandas as pd
import yfinance as yf
import numpy as np
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/analisis/{ticker}")
def obtener_analisis(ticker: str):
    try:
        df = yf.download(ticker, period="1y", interval="1d")
        if df.empty:
            raise HTTPException(status_code=404, detail="Ticker no encontrado")

        precios = df['Close'].values.flatten()
        retornos = np.diff(np.log(precios))
        
        var_95 = np.percentile(retornos, 5)
        cvar_95 = retornos[retornos <= var_95].mean()

        score = int(100 * (1 + cvar_95)) 
        
        if score > 70:
            status, color, signal = "COMPRA", "success", "Fuerza alcista detectada. Riesgo bajo."
        elif score > 40:
            status, color, signal = "MANTENER", "warning", "Neutralidad de mercado. Esperar confirmación."
        else:
            status, color, signal = "VENTA", "danger", "Alerta de riesgo. Salida recomendada."

        history = []
        for i, p in enumerate(precios[-30:]):
            history.append({"date": f"D{i+1}", "price": float(p)})

        return {
            "faro_score": score,
            "faro_status": status,
            "color_type": color,
            "signal": signal,
            "metrics": {"cvar_95": float(cvar_95)},
            "history": history
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
Añadir main.py versión backend V46.3 con URL para Vercel

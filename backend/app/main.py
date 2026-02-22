from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from app.engine import engine_v46p_brain
from app.ui import render_ui
import yfinance as yf
import pandas as pd

app = FastAPI(title="FARO Quant System V46.3")

@app.get("/", response_class=HTMLResponse)
async def index():
    return await render_ui([], "Neutro")

@app.post("/", response_class=HTMLResponse)
async def analyze(request: Request):

    form = await request.form()
    assets_input = form.get("assets")
    risk_level = form.get("risk_level")

    tickers = [t.strip().upper() for t in assets_input.split(",")]

    df = yf.download(tickers, period="2y")["Close"]

    if isinstance(df, pd.Series):
        df = df.to_frame()

    weights = [1/len(tickers)] * len(tickers)
    portfolio_dict = dict(zip(tickers, weights))

    result = engine_v46p_brain(df, portfolio_dict)

    return await render_ui(tickers, risk_level, result)

from fastapi import HTTPException
from pydantic import BaseModel
from typing import List

class EngineRequest(BaseModel):
    tickers: List[str]
    period: str = "2y"

@app.post("/api/run-engine")
async def run_engine_api(payload: EngineRequest):

    tickers = [t.upper() for t in payload.tickers]

    if len(tickers) == 0:
        raise HTTPException(status_code=400, detail="No tickers provided")

    df = yf.download(tickers, period=payload.period)["Close"]

    if df.empty:
        raise HTTPException(status_code=404, detail="No data found")

    if isinstance(df, pd.Series):
        df = df.to_frame()

    weights = [1/len(tickers)] * len(tickers)
    portfolio_dict = dict(zip(tickers, weights))

    result = engine_v46p_brain(df, portfolio_dict)

    return {
        "status": "success",
        "tickers": tickers,
        "metrics": result
    }

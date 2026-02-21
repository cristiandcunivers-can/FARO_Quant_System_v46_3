from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from metrics import obtener_analisis

app = FastAPI(title="FARO Quant API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # luego lo restringimos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "FARO Quant API running"}

@app.get("/analisis/{ticker}")
def analisis(ticker: str):
    return obtener_analisis(ticker)

@app.get("/health")
def health():
    return {"status": "ok"}
    
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "FARO Quant System running"}

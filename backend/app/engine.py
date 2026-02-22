# app/engine.py
import pandas as pd

def engine_v46p_brain(df: pd.DataFrame, portfolio_dict: dict) -> dict:
    """
    Motor de ejemplo.
    Calcula métricas básicas simuladas sobre df y portfolio.
    """
    # Simula algunos cálculos
    expected_return = round(df.mean().mean() * 0.001, 4)  # ejemplo
    volatility = round(df.std().mean() * 0.001, 4)
    sharpe_ratio = round(expected_return / (volatility + 1e-8), 2)
    
    return {
        "status": "motor ejecutado",
        "portfolio": portfolio_dict,
        "expected_return": expected_return,
        "volatility": volatility,
        "sharpe_ratio": sharpe_ratio
    }

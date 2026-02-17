import numpy as np
import pandas as pd

def get_faro_metrics(df):
    df_recent = df.tail(60)
    returns = df_recent['Close'].pct_change().dropna()
    
    if len(returns) < 10:
        raise ValueError("Datos insuficientes")

    volatility = returns.tail(20).std()
    recent_return = returns.tail(20).mean()
    
    var_95 = np.percentile(returns, 5)
    cvar_95 = returns[returns <= var_95].mean()
    
    score_base = 60
    boost_retorno = recent_return * 5000
    penalizacion_vol = volatility * 180
    
    faro_score = int(max(0, min(100, (score_base + boost_retorno - penalizacion_vol))))

    return {
        "volatility": float(volatility),
        "mean_return": float(recent_return),
        "cvar_95": float(cvar_95),
        "faro_score": faro_score,
        "window_days": len(df_recent)
    }
Añadir engine/metrics.py versión base V46.3

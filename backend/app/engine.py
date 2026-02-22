import pandas as pd
import numpy as np
from sklearn.covariance import LedoitWolf
from scipy.stats import t

def engine_v46p_brain(df: pd.DataFrame, portfolio_dict: dict):

    returns = df.pct_change().dropna()

    weights = np.array(list(portfolio_dict.values()))
    weights = weights / weights.sum()

    # Covarianza robusta Ledoit-Wolf
    lw = LedoitWolf()
    lw.fit(returns)
    cov_matrix = lw.covariance_

    mean_returns = returns.mean().values

    # Portfolio metrics
    portfolio_return = np.dot(weights, mean_returns)
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

    sharpe_ratio = portfolio_return / portfolio_volatility if portfolio_volatility != 0 else 0

    # Monte Carlo con t-Student
    simulations = 10000
    df_t = 3

    simulated_returns = t.rvs(df_t, size=simulations) * portfolio_volatility + portfolio_return

    var_95 = np.percentile(simulated_returns, 5)
    cvar_95 = simulated_returns[simulated_returns <= var_95].mean()

    return {
        "expected_return_annual": float(portfolio_return * 252),
        "volatility_annual": float(portfolio_volatility * np.sqrt(252)),
        "sharpe_ratio": float(sharpe_ratio * np.sqrt(252)),
        "cvar_95": float(cvar_95)
    }

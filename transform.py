import numpy as np

def add_features(df):
    
    df["Silver_ZAR"] = df["Silver_USD"] * df["USDZAR"]
    df["returns"] = df["Silver_ZAR"].pct_change()
    df["log_returns"] = np.log(df["Silver_ZAR"] / df["Silver_ZAR"].shift(1))
    
    df["gold_returns"] = np.log(df["Gold_USD"] / df["Gold_USD"].shift(1))
    df["sp500_returns"] = np.log(df["SP500"] / df["SP500"].shift(1))
    df["vix_changes"] = df["VIX"].pct_change()
    
    df["gold_silver_ratio"] = df["Gold_USD"] / df["Silver_USD"]
    
    df["fx_returns"] = np.log(df["USDZAR"] / df["USDZAR"].shift(1))
    df["fx_volatility"] = df["fx_returns"].rolling(7).std()
    
    df["MA_7"] = df["Silver_ZAR"].rolling(7).mean()
    df["MA_14"] = df["Silver_ZAR"].rolling(14).mean()
    df["MA_30"] = df["Silver_ZAR"].rolling(30).mean()
    df["MA_ratio_short"] = df["MA_7"] / df["MA_30"]
    
    df["momentum_7"] = df["Silver_ZAR"] - df["Silver_ZAR"].shift(7)
    df["momentum_14"] = df["Silver_ZAR"] - df["Silver_ZAR"].shift(14)
    
    df["volatility_7"] = df["log_returns"].rolling(7).std()
    df["volatility_14"] = df["log_returns"].rolling(14).std()
    df["volatility_ratio"] = df["volatility_7"] / df["volatility_14"]
    
    
    for lag in range(1, 8):
        df[f"lag_{lag}"] = df["Silver_ZAR"].shift(lag)
        df[f"return_lag_{lag}"] = df["log_returns"].shift(lag)
    
    
    df["gold_fx_interaction"] = df["gold_returns"] * df["fx_returns"]
    df["risk_interaction"] = df["sp500_returns"] * df["vix_changes"]
    
    df["target"] = df["log_returns"].shift(-1)
    
    df = df.replace([np.inf, -np.inf], np.nan)
    df = df.dropna()
    
    return df
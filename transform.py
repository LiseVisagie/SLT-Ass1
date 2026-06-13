import numpy as np

def add_features(df):
    
    df["Silver_ZAR"] = df["Silver_USD"] * df["USDZAR"]
    df["log_returns"] = np.log(df["Silver_ZAR"] / df["Silver_ZAR"].shift(1))
    
    for lag in range(1, 5):
        df[f"return_lag_{lag}"] = df["log_returns"].shift(lag)

    df["momentum_7"] = df["Silver_ZAR"] - df["Silver_ZAR"].shift(7)
    df["momentum_14"] = df["Silver_ZAR"] - df["Silver_ZAR"].shift(14)
    
    df["MA_ratio_short"] = df["Silver_ZAR"].rolling(7).mean() / df["Silver_ZAR"].rolling(30).mean()

    df["gold_returns"] = np.log(df["Gold_USD"] / df["Gold_USD"].shift(1))
    df["sp500_returns"] = np.log(df["SP500"] / df["SP500"].shift(1))
    df["fx_returns"] = np.log(df["USDZAR"] / df["USDZAR"].shift(1))
    df["brent_returns"] = np.log(df["Brent"] / df["Brent"].shift(1))
    df["dxy_returns"] = np.log(df["DXY"] / df["DXY"].shift(1))
    df["vix_changes"] = df["VIX"].pct_change()
    df["gold_silver_ratio"] = df["Gold_USD"] / df["Silver_USD"]
    
    df["gold_fx_interaction"] = df["gold_returns"] * df["fx_returns"]

    df["target_return"] = df["log_returns"].shift(-1)
    


    df["volatility_7"] = df["log_returns"].rolling(7).std()
    df["volatility_14"] = df["log_returns"].rolling(14).std()
    df["volatility_21"] = (df["log_returns"].rolling(21).std())
    df["volatility_63"] = (df["log_returns"].rolling(63).std())
    df["volatility_ratio"] = df["volatility_7"] / df["volatility_14"]
    
    df["gold_vol_21"] = (df["gold_returns"].rolling(21).std())
    df["sp500_vol_21"] = (df["sp500_returns"].rolling(21).std())
    df["fx_vol_21"] = df["fx_returns"].rolling(21).std()
    df["brent_vol_21"] = (df["brent_returns"].rolling(21).std())


    df["target_vol"] = (df["log_returns"].rolling(5).std().shift(-1))

    df = df.replace([np.inf, -np.inf], np.nan)
    df = df.dropna()
    
    return df
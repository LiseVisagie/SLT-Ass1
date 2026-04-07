import numpy as np

def add_features(df):
    
    df["Silver_ZAR"] = df["Silver_USD"] * df["USDZAR"]
    df["returns"] = df["Silver_ZAR"].pct_change()
    df["log_returns"] = np.log(df["Silver_ZAR"] / df["Silver_ZAR"].shift(1))
    df["MA_7"] = df["Silver_ZAR"].rolling(7).mean()
    df["MA_30"] = df["Silver_ZAR"].rolling(30).mean()
    df["volatility_7"] = df["log_returns"].rolling(7).std()
    df["target"] = df["log_returns"].shift(-1)
    df["inflation"] = np.log(df["US_CPI"] / df["US_CPI"].shift(1))
    df["rate_change"] = df["US_Interest_Rate"].diff()
    df["yield_change"] = df["US_10Y_Yield"].diff()
    df["unemployment_change"] = df["US_Unemployment"].diff()
    df["real_rate_proxy"] = df["US_Interest_Rate"] - df["inflation"]
    df["gold_real_rate"] = df["gold_returns"] * df["real_rate_proxy"]
    df["risk_macro_interaction"] = df["vix_changes"] * df["rate_change"]
    df = df.dropna()
    
    return df
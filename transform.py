import pandas as pd
import numpy as np

def add_features(df):
    
    # Convert to ZAR
    df["Silver_ZAR"] = df["Silver_USD"] * df["USDZAR"]
    
    # Returns
    df["returns"] = df["Silver_ZAR"].pct_change()
    
    # Log returns (better for modeling)
    df["log_returns"] = np.log(df["Silver_ZAR"] / df["Silver_ZAR"].shift(1))
    
    # Moving averages
    df["MA_7"] = df["Silver_ZAR"].rolling(7).mean()
    df["MA_30"] = df["Silver_ZAR"].rolling(30).mean()
    
    # Volatility
    df["volatility_7"] = df["log_returns"].rolling(7).std()
    
    # Drop NA values
    df = df.dropna()
    
    return df
import yfinance as yf
import pandas as pd
from datetime import datetime

def fetch_data(start_date="2015-01-01"):
    
    silver = yf.download("SI=F", start=start_date)
    fx = yf.download("ZAR=X", start=start_date)
    
    df = pd.DataFrame()
    df["Silver_USD"] = silver["Close"]
    df["USDZAR"] = fx["Close"]
    
    df = df.dropna()
    df.index.name = "Date"
    
    return df
import yfinance as yf
import pandas as pd
from pandas_datareader import data as pdr

def fetch_data(start_date="2025-01-01"):
    
    silver = yf.download("SI=F", start=start_date)
    fx = yf.download("ZAR=X", start=start_date)
    gold = yf.download("GC=F", start=start_date)
    sp500 = yf.download("^GSPC", start=start_date)
    vix = yf.download("^VIX", start=start_date)
    dxy = yf.download("DX-Y.NYB", start=start_date)
    brent = yf.download("BZ=F", start=start_date)

    df = pd.DataFrame()
    df["Silver_USD"] = silver["Close"]
    df["USDZAR"] = fx["Close"]
    df["Gold_USD"] = gold["Close"]
    df["SP500"] = sp500["Close"]
    df["VIX"] = vix["Close"]
    df["DXY"] = dxy["Close"]
    df["Brent"] = brent["Close"]
    
    macro = pd.DataFrame()
    macro["US_Interest_Rate"] = pdr.DataReader("FEDFUNDS", "fred", start_date)
    macro["US_10Y_Yield"] = pdr.DataReader("DGS10", "fred", start_date)


    df = df.join(macro, how="left")
    df = df.ffill()
    df = df.dropna()
    df.index.name = "Date"
    
    return df
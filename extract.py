import requests
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
    


    API_KEY = "3b99aac88e43596ece17437838d3bbaa"

    def get_fred_series(series_id, start_date="2025-01-01"):
        
        url = (
            "https://api.stlouisfed.org/fred/series/observations"
            f"?series_id={series_id}"
            f"&api_key={API_KEY}"
            "&file_type=json"
        )

        r = requests.get(url, timeout=60)
        r.raise_for_status()

        data = r.json()["observations"]

        df = pd.DataFrame(data)[["date", "value"]]

        df["date"] = pd.to_datetime(df["date"])
        df["value"] = pd.to_numeric(df["value"], errors="coerce")

        df = df[df["date"] >= start_date]

        return df.set_index("date")["value"]

    macro = pd.DataFrame()
    macro["US_Interest_Rate"] = get_fred_series("FEDFUNDS", start_date)
    macro["US_10Y_Yield"] = get_fred_series("DGS10", start_date)


    df = df.join(macro, how="left")
    df = df.ffill()
    df = df.dropna()
    df.index.name = "Date"
    
    return df
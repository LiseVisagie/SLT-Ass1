import pandas as pd
import os

def save_data(df, path="data/silver_data.csv"):
    
    if os.path.exists(path):
        existing = pd.read_csv(path, parse_dates=["Date"], index_col="Date")
        
        # Combine and remove duplicates
        df = pd.concat([existing, df])
        df = df[~df.index.duplicated(keep="last")]
    
    df.sort_index(inplace=True)
    df.to_csv(path)
    
    print(f"Data saved to {path}")
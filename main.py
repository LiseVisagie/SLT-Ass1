from extract import fetch_data
from transform import add_features
from load import save_data

def run_pipeline():
    
    print("Fetching data...")
    raw_data = fetch_data()
    
    print("Transforming data...")
    processed_data = add_features(raw_data)
    
    print("Saving data...")
    save_data(processed_data)
    
    print("Pipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()
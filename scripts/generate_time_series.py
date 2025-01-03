# generate_time_series.py

import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

# Generate synthetic time-series data
def generate_time_series(num_records=100, start_date="2023-01-01", freq="D"):
    # Generate date range
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    dates = [start_date + timedelta(days=i) for i in range(num_records)]

    # Generate random data
    data = {
        "Date": dates,
        "Value": np.random.rand(num_records) * 100  # Random values between 0 and 100
    }

    # Create the data directory if it doesn't exist
    os.makedirs("data", exist_ok=True)

    # Save the data to a CSV file
    file_path = os.path.join("data", "synthetic_time_series.csv")
    pd.DataFrame(data).to_csv(file_path, index=False)
    print(f"Time-series dataset successfully saved to {file_path}")

# generate_users.py

import pandas as pd
from faker import Faker
import os

# Initialize Faker
fake = Faker()

# Generate synthetic user data
def generate_user_data(num_records=100):
    data = {
        "Name": [fake.name() for _ in range(num_records)],
        "Email": [fake.email() for _ in range(num_records)],
        "Age": [fake.random_int(min=18, max=60) for _ in range(num_records)],
        "City": [fake.city() for _ in range(num_records)],
    }
    
    # Create the data directory if it doesn't exist
    os.makedirs("data", exist_ok=True)

    # Save the data to a CSV file
    file_path = os.path.join("data", "synthetic_user_data.csv")
    pd.DataFrame(data).to_csv(file_path, index=False)
    print(f"Dataset successfully saved to {file_path}")

# main.py

# Importing necessary modules from scripts
from scripts.generate_users import generate_user_data
from scripts.generate_time_series import generate_time_series
from scripts.generate_images import generate_images

def main():
    print("Welcome to the Dataset Generator!")
    print("1. Generate User Data")
    print("2. Generate Time-Series Data")
    print("3. Generate Synthetic Images")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        num_records = int(input("Enter the number of records to generate: "))
        print("Generating synthetic user dataset...")
        generate_user_data(num_records)
        print("Dataset generated and saved in the data folder!")
    elif choice == "2":
        num_records = int(input("Enter the number of time-series records to generate: "))
        print("Generating synthetic time-series dataset...")
        generate_time_series(num_records)
        print("Time-series dataset generated and saved in the data folder!")
    elif choice == "3":
        num_images = int(input("Enter the number of images to generate: "))
        print("Generating synthetic images...")
        generate_images(num_images)
        print("Synthetic images generated and saved in the data folder!")
    elif choice == "4":
        print("Exiting the Dataset Generator. Goodbye!")
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Dataset Generator for AI Prototyping

## **Overview**
This project is a flexible and reusable **Dataset Generator** designed to create synthetic datasets for AI applications. It provides an easy way to generate user data for testing, training, and validating machine learning models. With modular scripts and a testing notebook, this tool enables rapid prototyping of AI workflows without relying on sensitive or proprietary datasets.


## **Features**
- **Synthetic Data Generation**: Creates datasets with realistic names, emails, ages, and cities using the `Faker` library.
- **Modular Design**: Easily extendable scripts to include domain-specific data generation.
- **Jupyter Notebook Integration**: Provides an interactive way to test and inspect generated data.
- **Data Privacy**: Uses synthetic data to avoid concerns with real-world data sensitivity.
- **Customization**: Configure the number of records and data fields as per your requirements.


## **Project Structure**
```
Directory structure:
└── CodeHive-by-Jay-Dataset-Generator-For-CodeHive/
    ├── README.md
    ├── LICENSE
    ├── main.py
    ├── requirements.txt
    ├── notebooks/
    │   └── generate_and_test.ipynb
    └── scripts/
        ├── generate_images.py
        ├── generate_time_series.py
        └── generate_users.py
```


## **Setup Instructions**

### 1. **Clone the Repository**
```bash
$ git clone [<repository-url>](https://github.com/CodeHive-by-Jay/Dataset-Generator-For-CodeHive)
$ cd Dataset-Generator-For-CodeHive
```

### 2. **Install Dependencies**
Ensure you have Python 3.7+ installed. Install the required packages:
```bash
$ pip install -r requirements.txt
```

### 3. **Run the Dataset Generator**
Run the `main.py` script to start the generator:
```bash
$ python main.py
```


## **How to Use**

### **Generating Data**
1. Run the project using `main.py`. Select the option to generate user data.
2. Specify the number of records you want to create (default: 100).
3. The synthetic dataset will be saved in the `data/` directory as `synthetic_user_data.csv`.

### **Exploring Data**
1. Open the `notebooks/generate_and_test.ipynb` file in Jupyter Notebook.
2. Execute the notebook to generate and inspect the data.
3. Use the sample data to test machine learning models or preprocessing pipelines.


## **AI Use Cases**

### 1. **Training AI Models**
- Train supervised models (e.g., regression, classification) with synthetic data.
- Example: Predict user age based on other features like email domain and city.

### 2. **Data Augmentation**
- Combine synthetic data with real-world datasets to improve model generalization.

### 3. **Prototyping AI Applications**
- Prototype recommendation engines or chatbots using generated user profiles.

### 4. **NLP Tasks**
- Extend the tool to create synthetic text datasets for tasks like spam detection.

### 5. **Federated Learning**
- Simulate user data from multiple sources for federated learning experiments.


## **Customization Options**
- Modify `generate_users.py` to add new fields or customize data types (e.g., phone numbers, addresses).
- Extend the project to include datasets for specific domains (e.g., healthcare, finance).
- Add scripts for generating time-series or categorical data.


## **Dependencies**
- `Python 3.7+`
- `pandas`
- `faker`
- `jupyter`


## **Contributing**
Feel free to fork this repository and submit pull requests for:
- Adding new features.
- Optimizing code performance.
- Expanding AI use cases.


## **License**
This project is licensed under the MIT License.


## **Contact**
For questions or contributions, please reach out to:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/brayan-j4y)  
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/brayanj4y)  
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:souopsylvain@gmail.com) 



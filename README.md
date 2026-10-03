# 🏠 House Price Prediction Using Linear Regression

## 📌 About the Project

House Price Prediction is a Machine Learning project developed using **Python and Linear Regression**.

The main objective of this project is to predict the price of a house based on different property-related features such as area, number of bedrooms, bathrooms, location, and other relevant factors available in the dataset.

The project includes data preprocessing, exploratory data analysis, data visualization, feature processing, model training, model evaluation, and house price prediction.

---

## 🎯 Objective

The objectives of this project are:

* Analyze a housing dataset.
* Clean and preprocess the data.
* Handle missing values and duplicate records.
* Identify important features for house price prediction.
* Perform exploratory data analysis.
* Visualize relationships between housing features and price.
* Train a Linear Regression machine learning model.
* Evaluate the model using different performance metrics.
* Save the trained machine learning model.
* Provide an interface for predicting house prices.

---

## 📊 Dataset

The project uses a housing dataset containing property-related information.

The dataset contains features such as:

* House area/size
* Number of bedrooms
* Number of bathrooms
* Location
* Parking or other property features
* House price

> The exact features depend on the selected housing dataset.

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib
* Streamlit

### Tools

* Visual Studio Code
* Git
* GitHub

---

## 🔄 Project Workflow

```text
Housing Dataset
       ↓
Data Loading
       ↓
Data Inspection
       ↓
Data Cleaning
       ↓
Exploratory Data Analysis
       ↓
Data Visualization
       ↓
Feature Selection
       ↓
Categorical Encoding
       ↓
Train-Test Split
       ↓
Linear Regression
       ↓
Model Evaluation
       ↓
Save Trained Model
       ↓
House Price Prediction
```

---

## 🧹 Data Preprocessing

The following preprocessing steps are performed:

* Load the housing dataset using Pandas.
* Check the shape and structure of the dataset.
* Check data types.
* Identify missing values.
* Remove duplicate records.
* Separate numerical and categorical features.
* Encode categorical features using One-Hot Encoding.
* Prepare the data for machine learning.

---

## 📈 Exploratory Data Analysis

Exploratory Data Analysis is performed to understand the dataset and identify relationships between different features.

The project includes visualizations such as:

### 1. House Price Distribution

Shows the distribution of house prices in the dataset.

### 2. Area vs House Price

Shows the relationship between property area and house price.

### 3. Correlation Heatmap

Shows the correlation between numerical features.

### 4. Actual vs Predicted Prices

Compares the actual house prices with the prices predicted by the machine learning model.

---

## 🤖 Machine Learning Model

### Linear Regression

Linear Regression is used to predict house prices based on the selected property features.

The dataset is divided into:

* **80% Training Data**
* **20% Testing Data**

The model learns patterns from the training data and is then tested using unseen test data.

---

## 📊 Model Evaluation

The trained model is evaluated using:

### MAE — Mean Absolute Error

Measures the average absolute difference between actual and predicted prices.

### MSE — Mean Squared Error

Measures the average squared difference between actual and predicted prices.

### RMSE — Root Mean Squared Error

Measures prediction error in the same unit as the target price.

### R² Score

Measures how much of the variation in house prices is explained by the model.

The actual evaluation results are generated after training the model.

---

## 💾 Model Saving

The trained machine learning pipeline is saved using **Joblib**.

```text
models/house_price_model.pkl
```

The saved model can be loaded later to make predictions without retraining the model.

---

## 🖥️ Streamlit Application

The project includes a Streamlit-based interface for house price prediction.

The application allows users to:

1. Enter house/property details.
2. Submit the information.
3. Load the trained machine learning model.
4. Generate a predicted house price.
5. Display the estimated price.

---

## 📁 Project Structure

```text
House-Price-Prediction/
│
├── dataset/
│   ├── Housing - Housing.csv
│   └── cleaned_housing.csv
│
├── models/
│   └── house_price_model.pkl
│
├── outputs/
│   ├── price_distribution.png
│   ├── area_vs_price.png
│   ├── correlation_heatmap.png
│   └── actual_vs_predicted.png
│
├── src/
│   ├── data_analysis.py
│   ├── data_cleaning.py
│   ├── check_cleaned_data.py
│   ├── visualization.py
│   ├── train_model.py
│   ├── model_evaluation.py
│   └── predict.py
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/vaishnavisagare725/House-Price-Prediction.git
```

Open the project folder:

```bash
cd House-Price-Prediction
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run the Project

### Step 1 — Activate Virtual Environment

```bash
venv\Scripts\activate
```

### Step 2 — Train the Model

```bash
cd src
python train_model.py
```

### Step 3 — Run the Prediction Program

```bash
python predict.py
```

### Step 4 — Run the Streamlit Application

Go back to the project root:

```bash
cd ..
```

Run:

```bash
streamlit run app.py
```

The application will open in the browser.

---

## 🔮 Future Improvements

The project can be improved by:

* Using larger housing datasets.
* Trying other regression algorithms.
* Performing feature engineering.
* Applying hyperparameter tuning.
* Comparing multiple machine learning models.
* Improving the Streamlit user interface.
* Deploying the application online.
* Adding more location-based features.

---

## 🎓 Internship Project

This project was developed as part of a **Python Development Internship**.

### Project Domain

**Python Development / Machine Learning**

### Project

**House Price Prediction using Linear Regression**

---

## 👩‍💻 Author

**Vaishnavi Sagare**
Python Full Stack Developer

---

## ⭐ Skills Demonstrated

* Python
* Pandas
* NumPy
* Data Cleaning
* Data Analysis
* Data Visualization
* Machine Learning
* Linear Regression
* Scikit-learn
* Model Evaluation
* Joblib
* Streamlit
* Git
* GitHub

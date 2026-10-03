import pandas as pd
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split


# Load dataset
df = pd.read_csv("../dataset/cleaned_house_prices.csv")


X = df.drop("price", axis=1)
y = df["price"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Load trained model
model = joblib.load("../models/house_price_model.pkl")


# Predict
y_pred = model.predict(X_test)


# Plot
plt.figure(figsize=(8, 5))

plt.scatter(y_test, y_pred)

plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")

plt.title("Actual vs Predicted House Prices")

plt.savefig("../outputs/actual_vs_predicted.png")

plt.show()

print("Evaluation graph created successfully!")
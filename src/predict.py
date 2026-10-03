import pandas as pd
import joblib


# Load model
model = joblib.load("../models/house_price_model.pkl")


# Create sample house
house = pd.DataFrame([
    {
        "area": 5000,
        "bedrooms": 3,
        "bathrooms": 2,
        "stories": 2,
        "mainroad": "yes",
        "guestroom": "no",
        "basement": "no",
        "hotwaterheating": "no",
        "airconditioning": "yes",
        "parking": 2,
        "prefarea": "yes",
        "furnishingstatus": "semi-furnished"
    }
])


# Predict
prediction = model.predict(house)


print("Predicted House Price:", prediction[0])
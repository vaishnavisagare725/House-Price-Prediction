import streamlit as st
import pandas as pd
import joblib


# Load model
model = joblib.load("models/house_price_model.pkl")


# Page title
st.title("🏠 House Price Prediction")

st.write(
    "Enter the house details below to predict the estimated house price."
)


# Inputs
area = st.number_input(
    "Area (sq ft)",
    min_value=500,
    value=5000
)

bedrooms = st.number_input(
    "Number of Bedrooms",
    min_value=1,
    max_value=10,
    value=3
)

bathrooms = st.number_input(
    "Number of Bathrooms",
    min_value=1,
    max_value=10,
    value=2
)

stories = st.number_input(
    "Number of Stories",
    min_value=1,
    max_value=10,
    value=2
)

parking = st.number_input(
    "Number of Parking Spaces",
    min_value=0,
    max_value=10,
    value=2
)

mainroad = st.selectbox(
    "Main Road",
    ["yes", "no"]
)

guestroom = st.selectbox(
    "Guest Room",
    ["yes", "no"]
)

basement = st.selectbox(
    "Basement",
    ["yes", "no"]
)

hotwaterheating = st.selectbox(
    "Hot Water Heating",
    ["yes", "no"]
)

airconditioning = st.selectbox(
    "Air Conditioning",
    ["yes", "no"]
)

prefarea = st.selectbox(
    "Preferred Area",
    ["yes", "no"]
)

furnishingstatus = st.selectbox(
    "Furnishing Status",
    [
        "furnished",
        "semi-furnished",
        "unfurnished"
    ]
)


# Prediction button
if st.button("Predict House Price"):

    house = pd.DataFrame([
        {
            "area": area,
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "stories": stories,
            "mainroad": mainroad,
            "guestroom": guestroom,
            "basement": basement,
            "hotwaterheating": hotwaterheating,
            "airconditioning": airconditioning,
            "parking": parking,
            "prefarea": prefarea,
            "furnishingstatus": furnishingstatus
        }
    ])


    prediction = model.predict(house)


    st.success(
        f"Estimated House Price: ₹{prediction[0]:,.2f}"
    )
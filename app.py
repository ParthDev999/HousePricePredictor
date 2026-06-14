import streamlit as st
import joblib

model = joblib.load("models/house_price_model.pkl")

st.title("House Price Prediction App")

area = st.number_input("Area in sq ft", min_value=1)
bedrooms = st.number_input("Bedrooms", min_value=1, step=1)
bathrooms = st.number_input("Bathrooms", min_value=1, step=1)
age = st.number_input("Age of House", min_value=0, step=1)

if st.button("Predict Price"):
    new_house = [[area, bedrooms, bathrooms, age]]
    prediction = model.predict(new_house)[0]
    st.success(f"Predicted House Price: ₹{prediction:,.0f}")
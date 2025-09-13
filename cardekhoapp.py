import streamlit as st
import pandas as pd
import pickle

# Load the trained Random Forest model
model = pickle.load(open("best_model.pkl", "rb"))

st.title("🚗 Car Price Prediction (CarDekho)")

st.write("Enter car details to predict the selling price.")

# Input fields (adjust according to your dataset features)
year = st.number_input("Year", min_value=1990, max_value=2025, step=1)
km_driven = st.number_input("Kilometers Driven", min_value=0, max_value=3000000, step=1000)
fuel = st.selectbox("Fuel", ["Petrol", "Diesel", "CNG", "LPG", "Electric"])
seller_type = st.selectbox("Seller Type", ["Dealer", "Individual", "Trustmark Dealer"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.selectbox("Owner", ["First Owner", "Second Owner", "Third Owner", "Fourth & Above Owner", "Test Drive Car"])

# Prediction
if st.button("Predict Price"):
    input_df = pd.DataFrame([{
        "year": year,
        "km_driven": km_driven,
        "fuel": fuel,
        "seller_type": seller_type,
        "transmission": transmission,
        "owner": owner
    }])
    
    pred = model.predict(input_df)[0]
    st.success(f"💰 Estimated Selling Price: ₹ {pred:,.0f}")

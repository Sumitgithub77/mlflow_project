import streamlit as st
import joblib
import numpy as np

# Load your saved model pipeline
model = joblib.load("model/churn_model.pkl")

st.title("Telco Customer Churn Prediction")

# Input widgets for each feature
SeniorCitizen = st.selectbox("Senior Citizen", options=[0,1], format_func=lambda x: "Yes" if x==1 else "No")
tenure = st.number_input("Tenure (months)", min_value=0, max_value=72, value=12)
MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0, max_value=200.0, value=70.0)
TotalCharges = st.number_input("Total Charges", min_value=0.0, max_value=20000.0, value=500.0)

# AvgChargesPerMonth = TotalCharges / tenure
# To avoid division by zero:
AvgChargesPerMonth = TotalCharges / tenure if tenure > 0 else 0.0
st.write(f"Avg Charges Per Month: {AvgChargesPerMonth:.2f}")

HighMonthlyCharges = st.selectbox("High Monthly Charges (Above Median)", options=[0,1], format_func=lambda x: "Yes" if x==1 else "No")
LongTenure = st.selectbox("Long Tenure (Above 48 months)", options=[0,1], format_func=lambda x: "Yes" if x==1 else "No")

# Prepare input array in the correct order
input_data = np.array([[SeniorCitizen, tenure, MonthlyCharges, TotalCharges, AvgChargesPerMonth, HighMonthlyCharges, LongTenure]])

# When user clicks Predict
if st.button("Predict Churn"):
    prediction = model.predict(input_data)[0]
    prediction_proba = model.predict_proba(input_data)[0][1]

    st.markdown(f"**Churn Prediction:** {'Yes' if prediction == 1 else 'No'}")
    st.markdown(f"**Churn Probability:** {prediction_proba:.2%}")

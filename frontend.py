import streamlit as st
import requests

APP_URI = "http://localhost:8000/predict"

st.title("Insurance Premium Category Predictor")

st.markdown("Enter your details below:")

age = st.number_input("Age", min_value=0, max_value=119, value=30)
weight = st.number_input("Weight (kg)", min_value=0.0, value=70.0)
height = st.number_input("Height (cm)", min_value=0.0, value=170.0)
income_lpa = st.number_input("Annual Income (LPA)", min_value=0.0, value=5.0)
smoker = st.selectbox("Are you a smoker", options=[True, False])
city = st.text_input("City of Residence", value="Mumbai")
occupation = st.selectbox("Occupation", options=[
    'retired', 'freelancer', 'student', 'government_job',
    'business_owner', 'unemployed', 'private_job'
])

if st.button("Predict Premium Category"):
    user_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }
    
    try:
        response = requests.post(APP_URI, json=user_data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Insurance Premium Category: **{result['predicted_category']}")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        st.error("An error occurred while connecting to the prediction service.")

# command to run the app:
# streamlit run frontend.py
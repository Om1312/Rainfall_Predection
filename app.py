import streamlit as st
import numpy as np
import pickle

# -----------------------------
# Load Model
# -----------------------------
with open("rainfall_prediction_model.pkl", "rb") as f:
    saved = pickle.load(f)

model = saved["model"]              # Extract trained model
feature_names = saved["feature_names"]  # Just for reference

st.title("🌧️ Rainfall Prediction App")
st.write("Enter weather values below to predict rainfall")

# -----------------------------
# Input Fields
# -----------------------------
pressure = st.number_input("Pressure", step=0.1)
dewpoint = st.number_input("Dew Point", step=0.1)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, step=1.0)
cloud = st.number_input("Cloud Cover (%)", min_value=0.0, max_value=100.0, step=1.0)
sunshine = st.number_input("Sunshine (hours)", step=0.1)
winddirection = st.number_input("Wind Direction (°)", min_value=0.0, max_value=360.0, step=1.0)
windspeed = st.number_input("Wind Speed (km/h)", step=0.1)

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict"):
    features = np.array([[pressure, dewpoint, humidity, cloud, sunshine, winddirection, windspeed]])

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("🌧️ Rainfall Expected")
    else:
        st.info("☀️ No Rainfall Expected")

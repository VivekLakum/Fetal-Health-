import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("fetal_model.pkl", "rb"))

st.title("👶 Fetal Health Prediction")
st.write("Enter the main indicators to predict fetal health")

# Main inputs
baseline = st.slider("Baseline Value", 80, 180, 120)
acc = st.slider("Accelerations", 0.0, 1.0, 0.1)
movement = st.slider("Fetal Movement", 0.0, 1.0, 0.1)
contractions = st.slider("Uterine Contractions", 0.0, 1.0, 0.1)
light_decel = st.slider("Light Decelerations", 0.0, 1.0, 0.0)
severe_decel = st.slider("Severe Decelerations", 0.0, 1.0, 0.0)

# Construct full input with default 0s for the rest
input_data = [0]*21  # assuming model expects 21 inputs
input_data[0] = baseline
input_data[1] = acc
input_data[2] = movement
input_data[3] = contractions
input_data[5] = light_decel
input_data[6] = severe_decel

# Predict
if st.button("Predict Fetal Health"):
    result = model.predict([input_data])
    label = ["Normal", "Suspect", "Pathological"]
    st.success(f"Predicted Fetal Health: {label[int(result[0])-1]}")

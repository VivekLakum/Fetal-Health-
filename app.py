import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("fetal_model.pkl", "rb"))

st.title("👶 Fetal Health Prediction")
st.write("Enter all 21 features to get the most accurate prediction")

# Input fields
input_names = [
    "baseline_value", "accelerations", "fetal_movement", "uterine_contractions",
    "prolongued_decelerations", "light_decelerations", "severe_decelerations",
    "abnormal_short_term_variability", "mean_value_of_short_term_variability",
    "percentage_of_time_with_abnormal_long_term_variability",
    "histogram_width", "histogram_min", "histogram_max", "histogram_number_of_peaks",
    "histogram_number_of_zeroes", "histogram_mode", "histogram_mean",
    "histogram_median", "histogram_variance", "histogram_tendency"
]

# Create input fields (number_input)
user_inputs = []
for name in input_names:
    val = st.number_input(f"{name.replace('_', ' ').capitalize()}", value=0.0, format="%.4f")
    user_inputs.append(val)

# Predict button
if st.button("🔍 Predict Fetal Health"):
    prediction = model.predict([user_inputs])
    label = ["Normal", "Suspect", "Pathological"]
    st.success(f"🧠 Predicted Fetal Health: **{label[int(prediction[0])-1]}**")

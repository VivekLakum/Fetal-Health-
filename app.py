import streamlit as st
import numpy as np
import pickle

# Load trained model
model = pickle.load(open("fetal_model.pkl", "rb"))

st.set_page_config(page_title="Fetal Health Predictor", layout="centered")
st.title("👶 Fetal Health Predictor")
st.write("Enter fetal measurements below to predict health status:")

# Define feature names
features = [
    'baseline_value', 'accelerations', 'fetal_movement', 'uterine_contractions',
    'light_decelerations', 'severe_decelerations', 'prolongued_decelerations',
    'abnormal_short_term_variability', 'mean_value_of_short_term_variability',
    'percentage_of_time_with_abnormal_long_term_variability',
    'mean_value_of_long_term_variability', 'histogram_width',
    'histogram_min', 'histogram_max', 'histogram_number_of_peaks',
    'histogram_number_of_zeroes', 'histogram_mode', 'histogram_mean',
    'histogram_median', 'histogram_variance', 'histogram_tendency'
]

# Create input fields dynamically
user_input = []
cols = st.columns(3)  # Display in 3 columns for better layout

for i, feature in enumerate(features):
    with cols[i % 3]:  # Cycle through the 3 columns
        val = st.number_input(f"{feature.replace('_', ' ').title()}", value=0.0, step=0.1)
        user_input.append(val)

# Predict button
if st.button("Predict Fetal Health"):
    input_array = np.array([user_input])
    prediction = model.predict(input_array)[0]

    if prediction == 1:
        st.success("🟢 Prediction: Normal")
    elif prediction == 2:
        st.warning("🟡 Prediction: Suspect")
    elif prediction == 3:
        st.error("🔴 Prediction: Pathological")
    else:
        st.info("Unable to determine prediction.")

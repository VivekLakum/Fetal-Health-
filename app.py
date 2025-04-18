import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score

# Load the trained model
model = pickle.load(open("fetal_model_smote.pkl", "rb"))


st.title("👶 Fetal Health Classifier")
st.write("Please enter all 21 feature values below 👇")

# List of all 21 features
features =[
  'baseline value',
  'accelerations',
  'fetal_movement',
  'uterine_contractions',
  'light_decelerations',
  'severe_decelerations',
  'prolongued_decelerations',
  'abnormal_short_term_variability',
  'mean_value_of_short_term_variability',
  'percentage_of_time_with_abnormal_long_term_variability',
  'mean_value_of_long_term_variability',
  'histogram_width',
  'histogram_min',
  'histogram_max',
  'histogram_number_of_peaks',
  'histogram_number_of_zeroes',
  'histogram_mode',
  'histogram_mean',
  'histogram_median',
  'histogram_variance',
  'histogram_tendency'
]


# Collect inputs
inputs = []
for feature in features:
    value = st.number_input(f"{feature.capitalize()}", value=0.0, format="%.4f")
    inputs.append(value)

# Prediction button
if st.button("🔍 Predict Fetal Health"):
    try:
        input_array = np.array(inputs).reshape(1, -1)  # Ensure 2D array
        prediction = model.predict(input_array)[0]
        label = ["Normal", "Suspect", "Pathological"]
        st.success(f"🧠 Predicted Fetal Health: **{label[int(prediction)-1]}**")
    except Exception as e:
        st.error(f"⚠️ Error during prediction: {e}")

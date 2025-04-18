import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score

# Load trained model
model = pickle.load(open("fetal_model.pkl", "rb"))

st.title("👶 Fetal Health Prediction")
st.write("Enter the main indicators to predict fetal health status")

# Use number_input instead of sliders
baseline = st.number_input("Baseline Value", min_value=80, max_value=200, value=120)
acc = st.number_input("Accelerations", min_value=0.0, max_value=1.0, value=0.1, format="%.3f")
movement = st.number_input("Fetal Movement", min_value=0.0, max_value=1.0, value=0.1, format="%.3f")
contractions = st.number_input("Uterine Contractions", min_value=0.0, max_value=1.0, value=0.1, format="%.3f")
light_decel = st.number_input("Light Decelerations", min_value=0.0, max_value=1.0, value=0.0, format="%.3f")
severe_decel = st.number_input("Severe Decelerations", min_value=0.0, max_value=1.0, value=0.0, format="%.3f")

# Prepare input data (21 features, rest are zero)
input_data = [0] * 21
input_data[0] = baseline
input_data[1] = acc
input_data[2] = movement
input_data[3] = contractions
input_data[5] = light_decel
input_data[6] = severe_decel

# Predict button
if st.button("🔍 Predict Fetal Health"):
    prediction = model.predict([input_data])
    label = ["Normal", "Suspect", "Pathological"]
    st.success(f"🧠 Predicted Fetal Health: **{label[int(prediction[0])-1]}**")

# Optional: Check test accuracy on sample dataset
if st.checkbox("📊 Run Test Accuracy Check"):
    test_df = pd.DataFrame([
        [120, 0.3, 0.1, 0.2, 0.0, 0.0],  # Normal
        [140, 0.1, 0.3, 0.3, 0.2, 0.0],  # Suspect
        [160, 0.0, 0.2, 0.4, 0.1, 0.1],  # Pathological
        [130, 0.4, 0.1, 0.1, 0.0, 0.0],  # Normal
        [110, 0.2, 0.4, 0.5, 0.0, 0.1]   # Pathological
    ], columns=[
        'baseline_value',
        'accelerations',
        'fetal_movement',
        'uterine_contractions',
        'light_decelerations',
        'severe_decelerations'
    ])

    true_labels = [1, 2, 3, 1, 3]  # expected classes

    full_data = []
    for row in test_df.values:
        row_data = [0] * 21
        row_data[0] = row[0]
        row_data[1] = row[1]
        row_data[2] = row[2]
        row_data[3] = row[3]
        row_data[5] = row[4]
        row_data[6] = row[5]
        full_data.append(row_data)

    preds = model.predict(full_data)
    acc = accuracy_score(true_labels, preds)
    st.info(f"✅ Accuracy on test data: **{acc * 100:.2f}%**")

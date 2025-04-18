import streamlit as st
import numpy as np
import pickle

# Page setup
st.set_page_config(page_title="Fetal Health Predictor", layout="centered")
# Background Image CSS
import base64

def set_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("data:image/png;base64,{encoded}");
             background-size: cover;
             background-repeat: no-repeat;
             background-attachment: fixed;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# Call this function
set_bg_from_local("images/my_fetal_bg.jpg")



st.title("👶 Fetal Health Classifier")
st.write("Please enter all 21 feature values below 👇")

# Load model
with open("fetal_model_smote.pkl", "rb") as f:
    model = pickle.load(f)

# Labels for 21 inputs
feature_labels = [
    "Baseline Value", "Accelerations", "Fetal Movement", "Uterine Contractions", "Light Decelerations",
    "Severe Decelerations", "Prolongued Decelerations", "Abnormal STV", "Mean STV", "% Time Abnormal LTV",
    "Mean LTV", "Histogram Width", "Histogram Min", "Histogram Max", "Histogram Peaks", "Histogram Zeroes",
    "Histogram Mode", "Histogram Mean", "Histogram Median", "Histogram Variance", "Histogram Tendency"
]

# Input grid
cols = st.columns(4)
inputs = []
missing = False

for i, label in enumerate(feature_labels):
    col = cols[i % 4]
    value = col.text_input(f"{label}", placeholder="Enter value")
    try:
        value = float(value)
        inputs.append(value)
    except:
        missing = True

# Predict
if st.button("🔍 Predict"):
    if missing or len(inputs) != 21:
        st.error("⚠️ Please fill in all 21 input values correctly.")
    else:
        X = np.array([inputs])
        prediction = model.predict(X)[0]

        if prediction == 1:
            st.success("🟢 Fetal Health Status: Normal")
            st.toast("Prediction: Normal 👶✅")
        elif prediction == 2:
            st.warning("🟡 Fetal Health Status: Suspect")
            st.toast("Prediction: Suspect ⚠️")
        else:
            st.error("🔴 Fetal Health Status: Pathological")
            st.toast("Prediction: Pathological 🚨")

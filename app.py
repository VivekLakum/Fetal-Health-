import streamlit as st
import numpy as np
import pickle

# Page setup
st.set_page_config(page_title="Fetal Health Predictor", layout="centered")
# Background Image CSS
def set_bg_from_url(url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background
set_bg_from_url("https://raw.githubusercontent.com/VivekLakum/Fetal-Health-/main/Screenshot%202025-04-18%20141639.png")



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
    st.info("Great! The fetal health appears to be normal. Keep up with regular check-ups and a healthy lifestyle.")

elif prediction == 2:
    st.warning("🟡 Fetal Health Status: Suspect")
    st.toast("Prediction: Suspect ⚠️")
    st.info("""
    ⚠️ The result is **Suspect**. It’s recommended to:
    - Repeat the test or consult your doctor
    - Monitor fetal movements and symptoms
    - Follow up with additional medical evaluations
    """)

else:
    st.error("🔴 Fetal Health Status: Pathological")
    st.toast("Prediction: Pathological 🚨")
    st.info("""
    🚨 **Immediate medical attention is advised.**
    
    The prediction indicates a potential issue with fetal health. Please:
    - Contact your healthcare provider as soon as possible
    - Avoid stress and keep yourself monitored
    - Follow prescribed diagnostic procedures (e.g., ultrasound, NST)
    """)


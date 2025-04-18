import streamlit as st
import numpy as np
import pickle

# Page setup
st.set_page_config(page_title="Fetal Health Predictor", layout="centered")
# Background Image CSS
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://drive.google.com/drive/home");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    h1, h2, h3, h4, h5, h6, .stMarkdown {
        color: white !important;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.7);
    }

    p, label, .css-1cpxqw2 {
        color: white !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.6);
    }
    </style>
""", unsafe_allow_html=True)


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

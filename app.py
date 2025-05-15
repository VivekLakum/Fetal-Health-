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

# Labels and help texts
feature_info = [
    ("Baseline Value", "Average fetal heart rate (bpm) over a period of time."),
    ("Accelerations", "Increases in fetal heart rate per second."),
    ("Fetal Movement", "Fetal body movements per second."),
    ("Uterine Contractions", "Frequency of uterine contractions per second."),
    ("Light Decelerations", "Small decreases in fetal heart rate per second."),
    ("Severe Decelerations", "Large decreases in fetal heart rate per second."),
    ("Prolong Decelerations", "Prolonged decreases in fetal heart rate per second."),
    ("Abnormal STV", "Abnormal short-term variability in fetal heart rate."),
    ("Mean STV", "Mean value of short-term variability."),
    ("% Time Abnormal LTV", "Percentage of time with abnormal long-term variability."),
    ("Mean LTV", "Mean long-term variability value."),
    ("Histogram Width", "Width of the heart rate histogram."),
    ("Histogram Min", "Minimum value in the histogram."),
    ("Histogram Max", "Maximum value in the histogram."),
    ("Histogram Peaks", "Number of peaks in the histogram."),
    ("Histogram Zeroes", "Number of zero values in the histogram."),
    ("Histogram Mode", "Most frequent value in the histogram."),
    ("Histogram Mean", "Average value in the histogram."),
    ("Histogram Median", "Middle value of the histogram."),
    ("Histogram Variance", "Statistical variance of the histogram."),
    ("Histogram Tendency", "Overall tendency of the histogram values.")
]

# Input grid
cols = st.columns(4)
inputs = []
missing = False

for i, (label, help_text) in enumerate(feature_info):
    col = cols[i % 4]
    value = col.text_input(f"{label}", placeholder="Enter value", help=help_text)
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

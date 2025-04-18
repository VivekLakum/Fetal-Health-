import streamlit as st
import pickle
import numpy as np

# Load the model
model = pickle.load(open("fetal_model.pkl", "rb"))

st.title("👶 Fetal Health Classifier")
st.write("Please enter all 21 feature values below 👇")

# List of all 21 features
features = [
    "baseline value", "accelerations", "fetal movement", "uterine contractions",
    "prolongued decelerations", "light decelerations", "severe decelerations",
    "abnormal short term variability", "mean short term variability",
    "percentage abnormal long term variability", "histogram width", "histogram min",
    "histogram max", "histogram number of peaks", "histogram number of zeroes",
    "histogram mode", "histogram mean", "histogram median", "histogram variance",
    "histogram tendency"
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

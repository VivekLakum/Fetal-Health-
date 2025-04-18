import streamlit as st
from predict import predict_fetal_health

st.set_page_config(page_title="Fetal Health Predictor", layout="centered")

st.title("👶 Fetal Health Prediction App")

menu = st.sidebar.selectbox("Navigate", ["🏠 Home", "🔍 Predict Fetal Health"])

if menu == "🏠 Home":
    st.header("Welcome to the Fetal Health Predictor 👶💓")
    st.write("""
    This AI-powered application predicts fetal health based on cardiotocographic features.

    You can:
    - 🔍 Predict the fetal health category (Normal, Suspect, Pathological)

    Select an option from the sidebar to begin!
    """)
    st.image("https://www.nicepng.com/png/full/252-2524392_fetus-png-pregnant-woman-silhouette-png.png", width=300)

elif menu == "🔍 Predict Fetal Health":
    predict_fetal_health()

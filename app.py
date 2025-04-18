import streamlit as st
from predict import predict_fetal_health
from about import show_about
from assistant import chat_assistant

# App Title
st.set_page_config(page_title="Fetal Health Predictor", layout="centered")

st.title("👶 Fetal Health Prediction App")

# Sidebar navigation
menu = st.sidebar.selectbox("Navigate", ["🏠 Home", "🔍 Predict Fetal Health", "💡 Assistant", "ℹ️ About"])

# Page handling
if menu == "🏠 Home":
    st.header("Welcome to the Fetal Health Predictor 👶💓")
    st.write("""
    This AI-powered application predicts fetal health based on cardiotocographic features.

    You can:
    - 🔍 Predict the fetal health category (Normal, Suspect, Pathological)
    - 💬 Talk to an assistant for help
    - ℹ️ Learn about fetal health and the features used

    Select an option from the sidebar to begin!
    """)
    st.image("https://www.nicepng.com/png/full/252-2524392_fetus-png-pregnant-woman-silhouette-png.png", width=300)

elif menu == "🔍 Predict Fetal Health":
    predict_fetal_health()

elif menu == "💡 Assistant":
    chat_assistant()

elif menu == "ℹ️ About":
    show_about()

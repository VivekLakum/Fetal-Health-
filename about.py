import streamlit as st

def show():
    st.title("📖 About Fetal Healthcare")
    
    st.image("https://img.freepik.com/premium-vector/fetus-medical-concept_118813-2670.jpg", width=400)

    st.markdown("""
    ### 🍼 What is Fetal Health?
    Fetal health refers to the well-being of a baby during pregnancy. Monitoring fetal health helps detect complications early and reduce risks for both the mother and the baby.

    ---
    ### 📊 What is CTG (Cardiotocography)?
    CTG is a test used during pregnancy to monitor:
    - **Fetal Heart Rate (FHR)**
    - **Uterine Contractions**
    
    Doctors use CTG data to understand how the baby is doing inside the womb.

    ---
    ### ⚠️ Fetal Health Categories:
    1. 🟢 **Normal** – Baby is doing well.
    2. 🟡 **Suspect** – Uncertain, needs more observation.
    3. 🔴 **Pathological** – Possible distress, medical action may be needed.

    These labels are assigned using clinical guidelines and machine learning models.

    ---
    ### 🤖 Why Use AI for Fetal Health?
    - Detect patterns from large datasets
    - Support doctors with fast, consistent predictions
    - Improve care in hospitals with fewer resources

    This app uses **21 features** from CTG data to predict fetal health using a trained AI model.

    ---
    ### ❤️ Final Note:
    This app is meant for **educational/demo purposes only.** Always consult a doctor for actual diagnosis or medical advice.

    > “Healthy mothers, healthy babies.” 👶❤️
    """)

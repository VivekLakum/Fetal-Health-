import streamlit as st
import numpy as np
import pickle

def show():
    st.markdown("<h1 style='text-align: center;'>👶 Fetal Health Classifier</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Enter the CTG features below to predict fetal health.</p>", unsafe_allow_html=True)

    with open("model/fetal_model.pkl", "rb") as f:
        model = pickle.load(f)

    # 4 columns layout
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        baseline_value = st.number_input("Baseline Value", help="Fetal heart rate baseline (in bpm)")
        uterine_contractions = st.number_input("Uterine Contractions", help="Contractions per second")
        severe_decelerations = st.number_input("Severe Decelerations", help="Deep heart rate drops per second")
        mean_stv = st.number_input("Mean STV", help="Mean value of Short-Term Variability")
        histogram_max = st.number_input("Histogram Max", help="Maximum fetal heart rate")
        histogram_mode = st.number_input("Histogram Mode", help="Most frequent value in histogram")

    with col2:
        accelerations = st.number_input("Accelerations", help="Number of fetal heart rate accelerations per second")
        light_decelerations = st.number_input("Light Decelerations", help="Mild heart rate dips per second")
        prolongued_decelerations = st.number_input("Prolongued Decelerations", help="Long heart rate drops per second")
        abnormal_ltv_pct = st.number_input("% Time Abnormal LTV", help="Percentage time with abnormal Long-Term Variability")
        histogram_peaks = st.number_input("Histogram Peaks", help="Number of peaks in histogram")
        histogram_mean = st.number_input("Histogram Mean", help="Mean heart rate from histogram")

    with col3:
        fetal_movement = st.number_input("Fetal Movement", help="Fetal movements per second")
        abnormal_short_term_variability = st.number_input("Abnormal STV", help="Abnormal Short-Term Variability (score)")
        mean_ltv = st.number_input("Mean LTV", help="Mean value of Long-Term Variability")
        histogram_width = st.number_input("Histogram Width", help="Width of fetal heart rate histogram")
        histogram_zeroes = st.number_input("Histogram Zeroes", help="Number of zeroes in histogram")
        histogram_median = st.number_input("Histogram Median", help="Median heart rate")

    with col4:
        histogram_min = st.number_input("Histogram Min", help="Minimum fetal heart rate")
        histogram_variance = st.number_input("Histogram Variance", help="Variance in heart rate")
        histogram_tendency = st.number_input("Histogram Tendency", help="Trend in heart rate")

    st.markdown("<br><div style='text-align: center;'>", unsafe_allow_html=True)
    if st.button("🔍 Predict"):
        features = np.array([[baseline_value, accelerations, fetal_movement, uterine_contractions,
                              light_decelerations, severe_decelerations, prolongued_decelerations,
                              abnormal_short_term_variability, mean_stv, abnormal_ltv_pct, mean_ltv,
                              histogram_width, histogram_min, histogram_max, histogram_peaks, histogram_zeroes,
                              histogram_mode, histogram_mean, histogram_median, histogram_variance, histogram_tendency]])

        prediction = model.predict(features)[0]

        if prediction == 1:
            st.success("🟢 Fetal Health Status: Normal")
            st.toast("Prediction: Normal 👶✅")
        elif prediction == 2:
            st.warning("🟡 Fetal Health Status: Suspect")
            st.toast("Prediction: Suspect ⚠️")
        else:
            st.error("🔴 Fetal Health Status: Pathological")
            st.toast("Prediction: Pathological 🚨")
    st.markdown("</div>", unsafe_allow_html=True)

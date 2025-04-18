import streamlit as st

def show():
    st.title("🤖 Ask the Fetal Health Assistant")
    st.markdown("Ask any question about fetal monitoring, features, or predictions!")

    # Keep chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Input box
    user_input = st.text_input("You:", placeholder="E.g., What is fetal movement?", key="chat_input")

    # Simple keyword-based response system
    def get_response(msg):
        msg = msg.lower()
        if "baseline" in msg:
            return "Baseline is the average fetal heart rate measured over a period. Normal range: 110–160 bpm."
        elif "accelerations" in msg:
            return "Accelerations are temporary increases in fetal heart rate, a good sign of fetal health."
        elif "decelerations" in msg:
            return "Decelerations are temporary drops in fetal heart rate. Severe/prolonged ones may indicate distress."
        elif "fetal movement" in msg:
            return "Fetal movement is how much the baby moves. Reduced movement may indicate a need for monitoring."
        elif "suspect" in msg:
            return "A 'Suspect' result means the fetal status is not clearly normal or pathological. More tests may be needed."
        elif "pathological" in msg:
            return "A 'Pathological' status means possible fetal distress. This requires medical attention."
        elif "features" in msg or "inputs" in msg:
            return "There are 21 features like fetal movement, accelerations, histogram values, etc., collected from CTG."
        elif "normal" in msg:
            return "A 'Normal' result means fetal heart activity is healthy and within safe ranges."
        elif "ctg" in msg:
            return "CTG stands for Cardiotocography, a method to record fetal heartbeat and contractions."
        else:
            return "I'm still learning that question. Try asking about a feature or prediction meaning!"

    # If user submits input
    if user_input:
        response = get_response(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Assistant", response))

    # Show chat history
    for sender, msg in st.session_state.chat_history:
        if sender == "You":
            st.markdown(f"🧍 **You:** {msg}")
        else:
            st.markdown(f"🤖 **Assistant:** {msg}")

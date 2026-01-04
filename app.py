import streamlit as st
from src.rag_pipeline import answer_question
from src.reminder import generate_reminder

st.set_page_config(page_title="MediMind", page_icon="💊")

# Session state for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = ""

# ---------------- LOGIN / SIGNUP ----------------
if not st.session_state.logged_in:
    st.title("💊 MediMind")
    st.subheader("Login / Signup")

    choice = st.radio("Select Option", ["Login", "Signup"])

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button(choice):
        if username and password:
            st.session_state.logged_in = True
            st.session_state.user = username
            st.success(f"{choice} successful!")
        else:
            st.warning("Please enter username and password")

# ---------------- MAIN APP ----------------
else:
    st.title(f"Welcome, {st.session_state.user} 👋")
    st.subheader("Medication Information Assistant")

    medicine = st.text_input("Enter Medicine Name")
    question = st.text_input("Ask a Question")

    if st.button("Get Information"):
        if medicine and question:
            response = answer_question(question, medicine)
            reminder = generate_reminder(medicine)

            st.markdown("### 🧠 Drug Information")
            st.text(response)

            st.markdown("### ⏰ Medication Reminder")
            st.json(reminder)
        else:
            st.warning("Please enter both medicine name and question.")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user = ""

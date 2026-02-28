import streamlit as st

st.set_page_config(page_title="Saarthi AI", layout="wide")

st.title("🌟 Saarthi AI – Inclusive Study Companion")
st.write("Learn Your Way – Hear It. See It. Understand It.")

concept = st.text_input("Enter a Concept (Example: Ohm's Law, Pointers, Photosynthesis)")

mode = st.radio(
    "Choose Learning Mode:",
    ["Beginner Mode", "Exam Mode", "Real-Life Mode"]
)

if st.button("Generate Explanation"):

    if concept == "":
        st.warning("Please enter a concept first.")
    else:
        st.subheader("📘 Explanation")

        if mode == "Beginner Mode":
            st.write(f"{concept} explained in very simple words.")
            st.write("• Easy definition")
            st.write("• Step-by-step explanation")
            st.write("• Simple example")

        elif mode == "Exam Mode":
            st.write(f"{concept} structured for exam writing.")
            st.write("• Proper definition")
            st.write("• Key points")
            st.write("• Important formula (if any)")

        elif mode == "Real-Life Mode":
            st.write(f"{concept} explained using real-life analogy.")
            st.write("• Practical example")
            st.write("• Daily life connection")

        st.subheader("📝 Practice Questions")
        st.write("1. What is the definition?")
        st.write("2. Explain with example.")
        st.write("3. Where is it used in real life?")

        st.subheader("♿ Accessibility Features")
        st.write("🔊 Text-to-Speech Support (For Blind Users)")
        st.write("🤟 Sign-Friendly Structured Format (For Deaf Users)")
        st.write("🧠 Mind Map View Available")

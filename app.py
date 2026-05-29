import streamlit as st
from utils import simplify_text, explain_words

st.set_page_config(
    page_title="Literature Companion",
    layout="wide"
)

st.title("📚 Literature Companion")
st.write("Understand classic literature in modern English.")

text = st.text_area(
    "Paste literary text here",
    height=300
)

if st.button("Simplify Text"):

    if not text.strip():
        st.warning("Please enter text.")

    else:

        with st.spinner("Simplifying..."):

            simplified = simplify_text(text)
            vocab = explain_words(text)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Original Text")
            st.write(text)

        with col2:
            st.subheader("Modern English")
            st.write(simplified)

        st.subheader("Difficult Words")
        st.text(vocab)
import streamlit as st
from src.rag.llm import question_answer

st.set_page_config(page_title="RO Tax Advisor", layout="centered")
st.title("RO Tax Advisor")
st.write("Pune o intrebare despre legistatia fiscala din Romania.")

question = st.text_input("Intrebare:", placeholder="Ex: Ce este TVA?")

if st.button("Trimite"):
    if question.strip():
        with st.spinner("Se proceseaza intrebarea..."):
            answer = question_answer(question)
        st.success("Raspuns:")
        st.write(answer)
    

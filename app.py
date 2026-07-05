import streamlit as st
from langchain_openai import ChatOpenAI

# API key from Streamlit secrets
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

# Initialize LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=OPENAI_API_KEY
)

# Streamlit UI
st.title("Text to Math Problem Solver")

# Session state
if "history" not in st.session_state:
    st.session_state.history = []

# Input
question = st.text_input("Enter your Math Problem")

# Button
if st.button("Solve"):
    if question:
        prompt = f"""
Solve the following math problem step-by-step:

Problem:
{question}
"""

        response = llm.invoke(prompt)
        answer = response.content

        st.session_state.history.append({
            "question": question,
            "answer": answer
        })

# Display history
st.subheader("Conversation History")

for i, item in enumerate(st.session_state.history, 1):
    st.write(f"**Question {i}:** {item['question']}")
    st.write(f"**Answer {i}:**")
    st.write(item["answer"])
    st.write("---")
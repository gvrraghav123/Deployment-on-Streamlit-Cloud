# import required libraries
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st

# load env variable
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Intialize llm
llm = ChatOpenAI(
    model = "gpt-3.5-turbo",
    temperature=0
)

# Streamlit Title
st.title("Text to Math Problem Solver")

# Create Session state
if "history" not in st.session_state:
    st.session_state.history = []

# User Input
question = st.text_input("Enter your Math Problem")

# Solve Button
if st.button("Solve"):
    if question:
        prompt = f"""
        Solve the following math problem step-by-step

        Problem:
        {question}
        """

        response = llm.invoke(prompt)

        answer = response.content

        # Store Question and Answer
        st.session_state.history.append(
            {
                "question":question,
                "answer":answer
            }
        )

# Display Conversation History
st.subheader("Conversation History")

for i, item in enumerate(st.session_state.history, start=1):
    st.write(f"**Question {i}:** {item['question']}")
    st.write(f"**Answer {i}:**")
    st.write(item["answer"])
    st.write("--")



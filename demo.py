import streamlit as st
from openai import OpenAI 


# Set your OpenAI API key
client = OpenAI(api_key = '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' )

st.title("GPT-based Chatbot")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a tutor and an assistant to help with test/quiz generation for an upper division intro to linguistics class (LIGN 101) taught at UCSD."},
    {"role": "user", "content": "What is language?"}
  ]
)
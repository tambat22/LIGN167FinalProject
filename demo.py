import streamlit as st
from openai import OpenAI 
import os
from dotenv import load_dotenv, find_dotenv

#load .env file 
load_dotenv(find_dotenv())

# Set your OpenAI API key
client = OpenAI(api_key = os.environ.get("OPENAI_API_KEY"))

st.title("GPT-based Chatbot")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a tutor and an assistant to help with test/quiz generation for an upper division intro to linguistics class (LIGN 101) taught at UCSD."},
    {"role": "user", "content": "What is language?"}
  ]
)

print(completion.choices[0].message)
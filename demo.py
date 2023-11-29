import streamlit as st
from openai import OpenAI
import openai
import os
from dotenv import load_dotenv, find_dotenv
import time

#run 'source .venv/bin/activate' on mac

#load .env file 
load_dotenv()

# Set your OpenAI API key
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

st.title("GPT-based Chatbot")

assistant = client.beta.assistants.retrieve("asst_BnvVyG8g4UpskXZzUPl8jIvp")

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="What topics were covered in the lecture for week 2: what is language?"
)

run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id="asst_BnvVyG8g4UpskXZzUPl8jIvp",
  instructions="Please address the user as User."
)

run_completed = False

print ("working")

while not run_completed:
    # Retrieve the run status
    run_status = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )

    # Check if the run has completed
    if run_status.status == "completed":  # Replace 'completed' with the actual attribute name
        run_completed = True
    else:
        # Wait for a short period before checking again
        time.sleep(1)  # Wait for 1 second

# Once the run is complete, retrieve and print messages
messages = client.beta.threads.messages.list(
    thread_id=thread.id
)

for message in messages:
    print(message)


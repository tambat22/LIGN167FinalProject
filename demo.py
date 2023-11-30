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
assistant = client.beta.assistants.retrieve("asst_BnvVyG8g4UpskXZzUPl8jIvp")

def api():
    thread = client.beta.threads.create()

    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content="What topics were covered in the lecture 2: what is language?"
    )

    run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id="asst_BnvVyG8g4UpskXZzUPl8jIvp",
    instructions="Please address the user as User."
    )

    run_completed = False

    while not run_completed:
        # Retrieve the run status
        run_status = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
        print(run_status.status)

        # Check if the run has completed
        if run_status.status == "completed":  # Replace 'completed' with the actual attribute name
            run_completed = True
        else:
            # Wait for a short period before checking again
            time.sleep(1)  # Wait for 1 second
        if (run_status.status == "failed"):
            print("failed")
            break

    # Once the run is complete, retrieve and print messages
    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )

def main():
    # Custom CSS to style the Streamlit app
    st.markdown("""
        <style>
            .css-hi6a2p {color: black !important;}
            .main { 
                background-color: #ADD8E6;  /* Light Blue Background */
            }
            h1 {
                color: black;
                text-align: center;
                font-size: 40px; /* Larger Font Size */
            }
            .stButton>button {
                display: block;
                margin: 0 auto;
                margin-bottom: 10px;
            }
            .stButton>button:hover {
                background-color: #87CEFA; /* Lighter blue on hover */
            }
            .css-2trqyj {
                justify-content: center;  /* Center content in the column */
                text-align:center;
            }
            .st-bf {
                width: 100%;  /* Expander to full width */
            }
            .st-bf:focus {
                background-color: #B0C4DE; /* Light steel blue on focus */
            }
        </style>
    """, unsafe_allow_html=True)

    st.sidebar.title("Welcome to LIGN 101: Introduction to Linguistics")
    st.sidebar.write("Please select an option below.")
    st.sidebar.write("Note that quiz and test will have a maximum of 100 questions.")
    st.sidebar.write("You will also be allowed to choose the range of week(s) from 0 - 10 to cover for each quiz/test.")
    st.sidebar.write("Press enter after each selection.")

    # Using session state to track which option was selected
    if 'option' not in st.session_state:
        st.session_state.option = None

    if st.sidebar.button("Generate Quiz"):
        st.session_state.option = 'quiz'
    if st.sidebar.button("Generate Test"):
        st.session_state.option = 'test'

    # Main page content based on sidebar selection
    if st.session_state.option == 'quiz':
        display_quiz_details()
    elif st.session_state.option == 'test':
        display_test_details()

def display_quiz_details():
    st.title("Quiz Details")
    num_questions_quiz = st.number_input("Number of Questions for Quiz", min_value=1, max_value=100, value=None, key='num_questions_quiz')
    start_week_quiz = st.number_input("Start Week for Quiz", min_value=1, max_value=10,value=None, key='start_week_quiz')
    end_week_quiz = st.number_input("End Week for Quiz", min_value=start_week_quiz, max_value=10, value=None,key='end_week_quiz')
    
    if (num_questions_quiz and start_week_quiz and end_week_quiz and 
        start_week_quiz <= end_week_quiz and num_questions_quiz <= 100 and end_week_quiz <= 10 and start_week_quiz >= 0):
        if st.button("Confirm Quiz Details", key='confirm_quiz'):
            st.write(f"Quiz with {num_questions_quiz} questions covering weeks {start_week_quiz} to {end_week_quiz} is being generated...")

def display_test_details():
    st.title("Test Details")
    num_questions_test = st.number_input("Number of Questions for Test", min_value=1, max_value=100, value=None, key='num_questions_test')
    start_week_test = st.number_input("Start Week for Test", min_value=1, max_value=10, value=None, key='start_week_test')
    end_week_test = st.number_input("End Week for Test", min_value=start_week_test, max_value=10, value=None, key='end_week_test')
    
    if (num_questions_test and start_week_test and end_week_test and 
        start_week_test <= end_week_test and num_questions_test <= 100 and end_week_test <= 10 and start_week_test >= 0):
        if st.button("Confirm Test Details", key='confirm_test'):
            st.write(f"Test with {num_questions_test} questions covering weeks {start_week_test} to {end_week_test} is being generated...")


if __name__ == "__main__":
    main()
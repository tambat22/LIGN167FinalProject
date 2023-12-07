import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv
import time
import json

#run 'source .venv/bin/activate' on mac
#$ streamlit run demo.py

#load .env file 
load_dotenv()

# Set your OpenAI API key
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'),organization=os.getenv('OPENAI_ORG_ID'))
assistant = client.beta.assistants.retrieve("asst_C3Iyis7iFQ0HP7PFseOl1zZz")

#assistant = client.beta.assistants.update(
#    "asst_C3Iyis7iFQ0HP7PFseOl1zZz",
#    instructions= "You are an Instructional Assistant for a Linguistics Professor. Your job is to generate practice questions that are based on the course materials that are in the attached files. You need to generate your own questions, do not directly copy questions from the provided material. The generated question should be on a scale of three levels of difficulty: easy, medium, and hard. Do NOT generate repeat questions. You should generate comprehensive questions based on the content from the weeks specified by the user and desired number of questions. Make sure to generate ALL QUESTIONS, and EXACTLY the number of questions specified. DO NOT prompt the user for further instructions. DO NOT say anything else or prompt them for anything other than the answer to the question. DO NOT ask the user for their desired difficulty, instead use your best judgement when determining the difficulty of the questions. DO NOT show the difficulty level of the questions to the user."
#)

#print(assistant)

def generate_api(question_type,questions, content, start_week, end_week, topic):
    thread = client.beta.threads.create()
    print("Thread Created")
    time.sleep(10)

    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content= ("Create a " + questions + " question " + question_type +" "+ content + " that only HAS EXACTLY " + questions + 
                  " questions that is about the " + topic + " from week " + start_week + " to " + 
                  " week " + end_week + ". If there is at least 2 total questions, make it so there is at least one of each type of " +question_type +". For a multiple choice type question, each question should be numbered and should each have letter options and a short answer type should be free response." + 
                  "Format it like a quiz/test hand out. Title it " + content + "Then show the questions and answer choices. After write 'Answers' and give me answer key for the questions"+ 
                  " Next write '''json followed by the JSON code for ONLY the multiple choice type questions in a a JSON format like this format: [{questions,  \"options\": [\"A) Noun\", \"B) Verb\", \"C) Adjective\", \"D) Pronoun\"], answer:}]. Make sure that the options have letter options as well." +
                  " DO NOT WRITE anything else after the JSON code and only give me the JSON code for multiple choice type questions")
    )
    print("Message Created")

    time.sleep(10)
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id="asst_C3Iyis7iFQ0HP7PFseOl1zZz"
    )
    print("First run created")

    time.sleep(10)
    run_status = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )
    print("Attempting to retrieve run")

    while run_status.status!= "completed":
        # Retrieve the run status
        run_status = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )

        time.sleep(10)
        print(run_status.status)
        
        if (run_status.status=="failed"):
            print("failed")
            break

    # Once the run is complete, retrieve and print messages
    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )

    content = messages.data[0].content[0].text.value
    print("Printing content of response:")
    #print(content)
    # Split the text into questions and answers
    parts = content.split("Answers")
    print(parts)
    parts2 = parts[1].split("```json")

    questions_text = parts[0]
    answers_text = parts2[0]
    json_text = parts2[1]

    #print(questions_text)
    #print(answers_text)
    #print(json_text)

    st.write(questions_text)
    content = [questions_text,answers_text,json_text]
    print("Run retrieved successfully")
    return content


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

            .st-bf:focus {
                background-color: #B0C4DE; /* Light steel blue on focus */
            }
        </style>
    """, unsafe_allow_html=True)

    st.sidebar.title("Welcome to LIGN 101: Introduction to Linguistics")
    st.sidebar.write("Please select an option below.")
    st.sidebar.write("Due to API usage limitations, the maximum number of questions will be limited to 25 questions")
    st.sidebar.write("You will also be allowed to choose the range of week(s) from 1 - 10 to cover for each quiz/test.")
    st.sidebar.write("Press enter after each selection and wait for running to finish loading.")

    # Using session state to track which option was selected
    if 'option' not in st.session_state:
        st.session_state.option = None

    def setPage():
        st.session_state.option = None
    def setQuiz():
        st.session_state.confirm_quiz = False
    
    if st.sidebar.button("Generate Quiz/Test", on_click=setQuiz):
        st.session_state.option = 'quiz'
    if st.sidebar.button("Practice Questions", key="practice"):
        st.session_state.option = 'practice'

    if st.session_state.option == 'quiz':
        display_quiz_details()
    if st.session_state.option == 'practice':
        take_practice_quiz()

    if st.session_state.get("confirm_quiz", False):
        if st.sidebar.button("Take "+ st.session_state.content_type, key="quizortest", on_click= setPage):
            display_quiz()
        elif st.session_state.option == 'take quiz/test':
            display_quiz()
            
def take_practice_quiz():
    content = st.empty()
    content.write("Generating question...")
    if 'current_question_index' not in st.session_state:
        st.session_state.current_question_index = 0
        st.session_state.correct_p_answers = 0
        st.session_state.current_p_answers = None
        st.session_state.current_p_question = None
        st.session_state.current_p_options = None
        st.session_state.practice_thread = None  # Initialize thread state
        st.session_state.next_question = False

        thread = client.beta.threads.create()
        st.session_state.practice_thread = thread.id
        print("Thread created")
        st.session_state.current_p_question, st.session_state.current_p_options, st.session_state.current_p_answers = practice_question_generation(st.session_state.practice_thread)
        content = st.empty()
        content2 = st.empty()

    # Display the current count
    content.write(f"Question: " + st.session_state.current_p_question)
    content2 = st.radio("Choose an answer:", st.session_state.current_p_options, key=f"question_{st.session_state.current_question_index}")
    
    col1, col2 = st.columns(2)

    if col2.button("Next Question"):
        st.session_state.current_question_index += 1
        if content2 == st.session_state.current_p_answers:
            st.session_state.correct_p_answers += 1
        print (st.session_state.current_question_index)
        st.session_state.current_p_question, st.session_state.current_p_options, st.session_state.current_p_answers = practice_question_generation(st.session_state.practice_thread)

    if col1.button("End Practice"):
        if content2 == st.session_state.current_p_answers:
            st.session_state.correct_p_answers += 1
        st.write(f"Practice Completed! You got {str(st.session_state.correct_p_answers)} out of {str(st.session_state.current_question_index + 1)} questions right.")



def display_quiz_details():
    #keep track if confirm quiz button is clicked
    if 'confirm_quiz' not in st.session_state:
        st.session_state.confirm_quiz = False
    #tracking download buttons
    if 'quiz_txt' not in st.session_state:
        st.session_state.quiz_txt = False
    if 'key_txt' not in st.session_state:
        st.session_state.key_txt= False

    st.title("Additional Details")
    # Radio button for options
    quiz_or_test = st.radio(
        "What would you like to generate?",
        ('Quiz', 'Test')
    )

    st.session_state.content_type = quiz_or_test

    st.write ("Select the type of questions you would like:")
    st.write("Note that if no option is selected, the question type will be defaulted to multiple choice ")
    multiple_choice = st.checkbox("Multiple Choice", key= "mc")
    short_answer = st.checkbox("Short Answer", key="short_answer")

    num_questions_quiz = st.number_input("Number of Questions for "+quiz_or_test, min_value=1, max_value=25, value=None, key='num_questions_quiz')
    start_week_quiz = st.number_input("Start Week for " +quiz_or_test, min_value=1, max_value=10, value=None, key='start_week_quiz')
    end_week_quiz = st.number_input("End Week for "+quiz_or_test, min_value=start_week_quiz, max_value=10, value=None, key='end_week_quiz')
    
    st.write ("Are there any specific topic(s) you want a heavier emphasis on?")
    # Dictionary to store the status of checkboxes
    checkbox_status = {
        "Syntax": False,
        "Phonetics": False,
        "Morphology": False,
        "Phonology": False,
        "Semantics and Pragmatics": False,
        "Language Families": False,
        "Theoretical Syntax": False,
        "Speech Production and Perception": False,
        "Linguistic Theory": False,
        "Practical Applications in Linguistics": False
    }

    # Function to update the list based on checkbox status
    def update_selected_topics():
        selected_topics = [topic for topic, checked in checkbox_status.items() if checked]
        return selected_topics

    # Splitting the layout into two columns
    col1, col2 = st.columns(2)

    # Creating checkboxes in each column
    topics = list(checkbox_status.keys())
    for i, topic in enumerate(topics):
        current_col = col1 if i < len(topics) / 2 else col2
        checkbox_status[topic] = current_col.checkbox(topic, value=checkbox_status[topic])

    # Updating and displaying the list of selected topics
    selected_topics = update_selected_topics()

    generate_content_message = st.empty()

    #default question type
    question_type = "multiple choice"

    if (multiple_choice and short_answer):
        question_type = "multiple choice and short answer"
    elif (short_answer):
        question_type = "short answer"
    
    topic = "general course material"

    if (selected_topics!=0):
        topic = topic + " but with an emphasis on the following topic(s): "
        for topic_clicked in selected_topics:
            topic = topic + ", " + topic_clicked

    if (num_questions_quiz and start_week_quiz and end_week_quiz and 
        start_week_quiz <= end_week_quiz and num_questions_quiz <= 25 and end_week_quiz <= 10 and start_week_quiz > 0):
        
        if st.button("Confirm "+quiz_or_test+" Details", key = "quiz"):
            generate_content_message.write(quiz_or_test + f" with {num_questions_quiz} question(s) covering weeks {start_week_quiz} to {end_week_quiz} is being generated...")
        
            st.session_state.content = generate_api(question_type, str(num_questions_quiz), quiz_or_test, str(start_week_quiz), str(end_week_quiz), topic)
            #st.session_state.content  = ["A","B","C"]
            generate_content_message.empty()
            st.session_state.confirm_quiz = True

        if st.session_state.get("confirm_quiz", False):
            # Check if content is already generated and stored in session_state
            if "content" in st.session_state:
                question_text, answers_text, json_text = st.session_state.content

                # Generate text files based on the stored content
                generate_txt_file(quiz_or_test, question_text)
                generate_txt_file("answers", "**Answers" + answers_text)

                # Removing the leading and trailing triple quotes
                json_string = json_text[:-3]
                print(json_string)

                st.session_state.json = json_string
                
                # Display the quiz if the button was clicked
                if st.session_state.get("quiz_started", False):
                   take_quiz(json_string,quiz_or_test)
                

        #reset app
        if st.button("Start Over"):
            st.session_state.confirm_quiz = False
            # Add any other state resets here
            st.rerun()  # This will rerun the script from top to reset the app

def display_quiz():
    st.write("Answer each question to the best of your ability!")
    if "content" in st.session_state:
        json_string = st.session_state.json
        print(json_string)
           
        # Now you can parse the JSON string
        try:
            quiz_data = json.loads(json_string)
            print("Data loads successfully")
            # Further processing...
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            quiz_data = json.loads(json_string)
        
        st.session_state.option = 'take quiz/test'
        quiz_or_test = st.session_state.content_type
        print("taking " + quiz_or_test)
        take_quiz(quiz_data,quiz_or_test)

def generate_txt_file(type,text):
        btn = st.download_button(
        label="Download " +type+ " as a .txt file",
        data=text,
        file_name=type+".txt",
        mime="text/plain",
        key = "download_"+type)

# Function to run the quiz
def take_quiz(questions, test_type):
    print ("taking quiz/test")
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
        st.session_state.correct_answers = 0
    question = questions[st.session_state.current_question]
    st.write(f"Question {st.session_state.current_question + 1}: {question['question']}")

    # The options are already formatted as a list
    user_answer = st.radio("Choose an answer:", question["options"], key=f"question_{st.session_state.current_question}")

    # Check if it's the last question
    is_last_question = st.session_state.current_question == len(questions) - 1
    button_label = "Submit "+test_type if is_last_question else "Next Question"

    if st.button(button_label):
        if user_answer == question["answers"]:
            st.session_state.correct_answers += 1
        if not is_last_question:
            st.session_state.current_question += 1
        else:
            st.write(f"Quiz Completed! You got {st.session_state.correct_answers} out of {len(questions)} questions right.")

def display_practice():
   # Initialize state variables
    if 'start_practice' not in st.session_state:
        st.session_state.start_practice = False
        st.session_state.current_question_index = 0
        st.session_state.correct_p_answers = None
        st.session_state.current_p_question = "TestQ"
        st.session_state.current_p_options = "A"
        st.session_state.practice_thread = None  # Initialize thread state
        st.session_state.next_question = False

    if st.button("Start Practice Questions") and not st.session_state.start_practice:
        st.session_state.start_practice = True

        # Create a thread only if it hasn't been created yet
        if st.session_state.practice_thread is None:
            thread = client.beta.threads.create()
            st.session_state.practice_thread = thread.id
            print("Thread created")
            #practice_question_generation(thread.id)

        if st.session_state.start_practice:     
            take_practice_quiz()
        

def practice_question_generation(thread):
    message = client.beta.threads.messages.create(
    thread_id=thread,
    role="user",
    content= ("Write '''json and write the JSON CODE for EXACTLY ONE multiple choice question about the content of the class from weeks 1 - 10. The answer options should have letter choices. Format the response in JSON like this format: [{\"question\",  \"options\":, \"answer\":}], and only give me the response in JSON format. For every response format it exactly like this and give me this output.")
    )

    print("Message Created for Practice")

    time.sleep(10)
    run = client.beta.threads.runs.create(
        thread_id=thread,
        assistant_id="asst_C3Iyis7iFQ0HP7PFseOl1zZz"
    )
    print("First run created")

    time.sleep(10)
    run_status = client.beta.threads.runs.retrieve(
        thread_id=thread,
        run_id=run.id
    )
    print("Attempting to retrieve run")

    while run_status.status!= "completed":
        # Retrieve the run status
        run_status = client.beta.threads.runs.retrieve(
            thread_id=thread,
            run_id=run.id
        )

        time.sleep(10)
        print(run_status.status)
        
        if (run_status.status=="failed"):
            print("failed")
            break

    # Once the run is complete, retrieve and print messages
    messages = client.beta.threads.messages.list(
        thread_id=thread
    )

    content = messages.data[0].content[0].text.value
    part1 = content.split("'''json")
    part1 = part1[0].split("'''")
    print("loading json")
    print(part1[0])
    json_string = part1[0]
    question_data = json.loads(json_string)
    for item in question_data:
        questions = item['question']
        options = item['options']
        answer = item['answer']

    return questions, options, answer


if __name__ == "__main__":
    main()
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
assistant2 = client.beta.assistants.retrieve("asst_kO68ZsnTzqtfhLaHTMws9dsF")
def generate_api(question_type,questions, content, start_week, end_week, topic):
    thread = client.beta.threads.create()
    print("Thread Created")
    time.sleep(10)

    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content= ("Create a " + questions + " question " + question_type + content + " that only HAS EXACTLY " + questions + 
                  " questions that is about the " + topic + " from week " + start_week + " to " + 
                  " week " + end_week + ". A quiz should be easier than a test. Format it as a " + content + 
                  " handout with questions and option choices in a new line, and then write 'Answers' and give me answer key for the questions"+ 
                  " Then you MUST write 'JSON code' followed by JSON code for the quiz in a a JSON format following: [{questions,options,answers}]")
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
    # Split the text into questions and answers
    print("CONTEBT")
    print(content)
    parts = content.split("Answers:")
    parts2 = content.split("```json")

    questions_text = parts[0]
    answers_text = parts[1] if len(parts) > 1 else ""
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

    if st.sidebar.button("Generate Quiz/Test"):
        st.session_state.option = 'quiz'
    if st.sidebar.button("Generate Adaptive Quiz"):
        st.session_state.option = 'adaptive'
    # Main page content based on sidebar selection
    if st.session_state.option == 'quiz':
        display_quiz_details()
    if st.session_state.option == 'adaptive':
        print("INTERACTIVE QUIZ SELECTED")
        display_interactive_quiz_details()


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
    st.write("Would you like to generate a quiz or test?")
    quiz = st.checkbox("Quiz", key= "quizz")
    test = st.checkbox("Test", key="test")
    st.write ("Select the type of questions you would like:")
    st.write("Note that if no option is selected, the question type will be defaulted to multiple choice ")
    multiple_choice = st.checkbox("Multiple Choice", key= "mc")
    short_answer = st.checkbox("Short Answer", key="short_answer")

    num_questions_quiz = st.number_input("Number of Questions for Quiz", min_value=1, max_value=25, value=None, key='num_questions_quiz')
    start_week_quiz = st.number_input("Start Week for Quiz", min_value=1, max_value=10, value=None, key='start_week_quiz')
    end_week_quiz = st.number_input("End Week for Quiz", min_value=start_week_quiz, max_value=10, value=None, key='end_week_quiz')
    
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
        
        if st.button("Confirm Quiz Details", key = "quiz"):
            st.session_state.confirm_quiz = True
            generate_content_message.write(f"Quiz with {num_questions_quiz} question(s) covering weeks {start_week_quiz} to {end_week_quiz} is being generated...")
        
            st.session_state.content = generate_api(question_type, str(num_questions_quiz), "Quiz", str(start_week_quiz), str(end_week_quiz), topic)
            #st.session_state.content  = ["A","B","[{\"question\": \"Which of the following best describes the aspects used to describe consonants in phonetics?\", \"options\": {\"A\": \"Place, Manner\", \"B\": \"Voice, Manner\", \"C\": \"Place, Voice\", \"D\": \"Place, Manner, Voice\"}, \"answer\": \"D\"}]```"] 
            generate_content_message.empty()

        if st.session_state.get("confirm_quiz", False):
            # Check if content is already generated and stored in session_state
            if "content" in st.session_state:
                question_text, answers_text, json_text = st.session_state.content

                # Generate text files based on the stored content
                generate_txt_file("quiz", question_text)
                generate_txt_file("answers", "**Answers" + answers_text)

                # Removing the leading and trailing triple quotes
                json_string = json_text.strip("```")

                # Now you can parse the JSON string
                try:
                    quiz_data = json.loads(json_string)
                    print("Data loads successfully")
                    # Further processing...
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
                    quiz_data = json.loads(json_text)

                # Button to start the quiz
                if st.button("Take Quiz"):
                    st.session_state.quiz_started = True

                # Display the quiz if the button was clicked
                if st.session_state.get("quiz_started", False):
                    take_quiz(quiz_data)


        #reset app
        if st.button("Start Over"):
            st.session_state.confirm_quiz = False
            # Add any other state resets here
            st.rerun()  # This will rerun the script from top to reset the app

def generate_txt_file(type,text):
        btn = st.download_button(
        label="Download " +type+ " as a .txt file",
        data=text,
        file_name=type+".txt",
        mime="text/plain",
        key = "download_"+type)
# Function to run the quiz
def take_quiz(questions):
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
        st.session_state.correct_answers = 0

    question = questions[st.session_state.current_question]
    st.write(f"Question {st.session_state.current_question + 1}: {question['question']}")

    # Format the options for display
    options = question["options"]
    formatted_options = [f"{key}: {value}" for key, value in options.items()]
    user_answer_key = st.radio("Choose an answer:", formatted_options, key=f"question_{st.session_state.current_question}")

    # Check if it's the last question
    is_last_question = st.session_state.current_question == len(questions) - 1
    button_label = "Submit Quiz" if is_last_question else "Next Question"

    if st.button(button_label):
        # Extract the key from the selected answer
        selected_key = user_answer_key.split(":")[0]
        if selected_key == question["answer"]:
            st.session_state.correct_answers += 1
        if not is_last_question:
            st.session_state.current_question += 1
            st.experimental_rerun()
        else:
            st.write(f"Quiz Completed! You got {st.session_state.correct_answers} out of {len(questions)} questions right.")
            st.write(f"Number of incorrect answers: {len(questions) - st.session_state.correct_answers}")


    
    #create assistant thread
    #while loop 
    # send request
    #compare answer and send new request
    #Run one more time Give m
    #keep track of difficulty
def interactive_test(thread,question_number,numQuestions,topics):
    print("thread created")
    time.sleep(10)
    #TODO Make questions use topic from argument instead of hard coding
    gpt_query = "Give me a practice question on either the topic of japanese syntax or turkish syntax. Then you MUST write 'JSON code' followed by JSON code for the quiz in a a JSON format following: [{question,options,solution and detailed explanation}]." \
    
    if question_number == 0:
        gpt_query = "Give me a SINGLE practice question on either syntax. DO NOT GIVE ME MORE THAN ONE QUESTION. Then you MUST write 'JSON code' followed by JSON code for the quiz in a a JSON format following: [{question,options,solution and detailed explanation}]."
    elif question_number == numQuestions:
        gpt_query = "Give me a detailed breakdown of my performance, like the number of questions I got correct/incorrect as well as a detailed study plan and resources to improve my performance."
    else:
        gpt_query = "Give me a SINGLE practice question on either the topic of japanese syntax or turkish syntax. Give me a question of hard difficulty. MAKE SURE YOU DO NOT GIVE ME A QUESTION THAT YOU HAVE ASKED BEFORE. Then you MUST write 'JSON code' followed by JSON code for the quiz in a a JSON format following: [{question,options,solution and detailed explanation}]."
    
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content = gpt_query)
    print("message created")
    time.sleep(10)
    
    run = client.beta.threads.runs.create(
        thread_id = thread.id,
        assistant_id = "asst_kO68ZsnTzqtfhLaHTMws9dsF"
    )    
    print("First run created")
    time.sleep(10)
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    
    print("attempting to retrieve run ")
    #wait until run is completed
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
    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )
    content = messages.data[0].content[0].text.value
    # Split the text into questions and answers
    # parts = content.split("Answers:")
    # parts2 = content.split("```json")

    # questions_text = parts[0]
    # answers_text = parts[1] if len(parts) > 1 else ""
    # json_text = parts2[1]
    print("PRINTING PARTS ____________________________")
    print(content)
    return content     
        
def display_interactive_quiz_details():
    thread = client.beta.threads.create()
    print("created ThrEAD")
    
    
    #keep track if confirm quiz button is clicked
    if 'confirm_interactive_quiz' not in st.session_state:
        st.session_state.confirm_interactive_quiz = False

    st.title("Additional Details")
    #ONLY MC QUESTIONS FOR ADAPTIVE TEST 
    with st.form('quiz_properties'):
        num_questions_quiz = st.number_input("Number of Questions for Quiz", min_value=1, max_value=5, value=None, key='num_questions_quiz')
        start_week_quiz = st.number_input("Start Week for Quiz", min_value=1, max_value=10, value=None, key='start_week_quiz')
        end_week_quiz = st.number_input("End Week for Quiz", min_value=start_week_quiz, max_value=10, value=None, key='end_week_quiz')
    
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

        # Splitting the layout into two columns
        col1, col2 = st.columns(2)

        # Creating checkboxes in each column
        topics = list(checkbox_status.keys())
        for i, topic in enumerate(topics):
            current_col = col1 if i < len(topics) / 2 else col2
            checkbox_status[topic] = current_col.checkbox(topic, value=checkbox_status[topic])

        start_interactive_quiz = st.form_submit_button('Confirm Quiz Details')

        # Updating and displaying the list of selected topics
        selected_topics = [topic for topic, checked in checkbox_status.items() if checked]
        

        generate_content_message = st.empty()

        #default question type
        question_type = "multiple choice"
        
        topic = "general course material"

        if (selected_topics!=0):
            topic = topic + " but with an emphasis on the following topic(s): "
            for topic_clicked in selected_topics:
                topic = topic + ", " + topic_clicked
    
    if (num_questions_quiz and start_week_quiz and end_week_quiz and 
        start_week_quiz <= end_week_quiz and num_questions_quiz <= 25 and end_week_quiz <= 10 and start_week_quiz > 0):
        if start_interactive_quiz:
            take_interactive_quiz(num_questions_quiz,topic)
            # if st.button("Confirm Quiz Details", key = "quiz"):
            #     # st.session_state.confirm_quiz = True
            #     # generate_content_message.write(f"Quiz with {num_questions_quiz} question(s) covering weeks {start_week_quiz} to {end_week_quiz} is being generated...")
            
            #     # st.session_state.content = generate_api(question_type, str(num_questions_quiz), "Quiz", str(start_week_quiz), str(end_week_quiz), topic)
            #     # #st.session_state.content  = ["A","B","[{\"question\": \"Which of the following best describes the aspects used to describe consonants in phonetics?\", \"options\": {\"A\": \"Place, Manner\", \"B\": \"Voice, Manner\", \"C\": \"Place, Voice\", \"D\": \"Place, Manner, Voice\"}, \"answer\": \"D\"}]```"] 
            #     # generate_content_message.empty()
            #     take_interactive_quiz(num_questions_quiz,topic)

            # if st.session_state.get("confirm_quiz", False):
            #     # Check if content is already generated and stored in session_state
            #     if "content" in st.session_state:
            #         question_text, answers_text, json_text = st.session_state.content
                    
            #         # Removing the leading and trailing triple quotes
            #         json_string = json_text.strip("```")

            #         # Now you can parse the JSON string
            #         try:
            #             quiz_data = json.loads(json_string)
            #             print("Data loads successfully")
            #             # Further processing...
            #         except json.JSONDecodeError as e:
            #             print(f"Error decoding JSON: {e}")
            #             quiz_data = json.loads(json_text)

            #         # Button to start the quiz
            #         if st.button("Take Quiz"):
            #             st.session_state.interactive_quiz_started = True

            #         # Display the quiz if the button was clicked
            #         if st.session_state.get("interactive_quiz_started", False):
            #             print("ABOOUT TO TAKE INTERACTIVE QUIZ")
            #             take_interactive_quiz(num_questions_quiz,topic)


            # #reset app
            # if st.button("Start Over"):
            #     st.session_state.confirm_interactive_quiz = False
            #     # Add any other state resets here
            #     st.rerun()  # This will rerun the script from top to reset the app
def take_interactive_quiz(numQuestions,topics):
    thread = client.beta.threads.create()
    with st.form("quiz_questions"):
        difficulties = {1 : "easy", 2 : "medium", 3 : "hard"}
        if 'current_question' not in st.session_state:
            st.session_state.current_question = 0
            st.session_state.correct_answers = 0
        if 'latest_response' not in st.session_state: 
            st.session_state.latest_response = ""
            st.session_state.current_difficulty = 1
        
        #generate current question 
        st.session_state.latest_response = test_response()
        #interactive_test(thread,st.session_state.current_question,numQuestions,topics)
        question = parse_interactive_json(st.session_state.latest_response)[0]
        print("PARSED QUESTION")
        print(question)
        # print(question)
        # question = questions[st.session_state.current_question]
        st.write(f"Question {st.session_state.current_question + 1}: {question['question']}")

        # # Format the options for display
        options = question["options"]
        formatted_options = [f"{key}: {value}" for key, value in options.items()]
        user_answer_key = st.radio("Choose an answer:", formatted_options, key=f"question_{st.session_state.current_question}")

        # Check if it's the last question
        is_last_question = st.session_state.current_question == numQuestions - 1
        button_label = "Submit Quiz" if is_last_question else "Next Question"

        if st.button(button_label):
            # Extract the key from the selected answer
            selected_key = user_answer_key.split(":")[0]
            print(selected_key)
            if selected_key == question["answer"]:
                st.session_state.correct_answers += 1
            if not is_last_question:
                st.session_state.current_question += 1
                st.write("NEXT QUESTION!!")
                #st.experimental_rerun()
            else:
                #st.write(f"Quiz Completed! You got {st.session_state.correct_answers} out of {len(questions)} questions right.")
                #st.write(f"Number of incorrect answers: {len(questions) - st.session_state.correct_answers}")
                #completion = st.session_state.latest_response
                st.write("QUIZ COMPLETED!!")

def test_response():
    return """  Now, here is the JSON code for the quiz: 
```json[{"question": "What is the default word order in Turkish?","options": {"a": "Subject-Object-Verb (SOV)","b": "Subject-Verb-Object (SVO)", \
"c": "Verb-Subject-Object (VSO)", "d": "Verb-Object-Subject (VOS)"}, "solution": "a","explanation": "The default word order in Turkish is Subject-Object-Verb (SOV). This means that the subject comes first, followed by the object, and then the verb."}]```
"""

def parse_interactive_json(response):
    json_string = response.split("```json")[1].split("```")[0]
    try:
        res = json.loads(json_string)
        print("Interactive Json parsed successfully")
        # Further processing...
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        res = json.loads(json_string)
    return res
    
if __name__ == "__main__":
    # gen_api_test("10","Test","0","10","morphology")
    # interactive_test()
    main()
    #main()
    
    
    
#Have a loop that runs up until the number of questions the user requested for 
#Send request for problem and solution with gpt 
#Check if user's answer matches GPT's asnwer 
#Display Solution
#If user gets it correct, increase difficulty, user gets it incorrect, decrease difficulty, suer 
#When user clicks next, repeat
import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv
import time
import json
from collections import deque


#run 'source .venv/bin/activate' on mac
#$ streamlit run demo.py

#load .env file 
load_dotenv()

# Set your OpenAI API key
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'),organization=os.getenv('OPENAI_ORG_ID'))
assistant = client.beta.assistants.retrieve("asst_C3Iyis7iFQ0HP7PFseOl1zZz")

#assistant = client.beta.assistants.update(
# "asst_C3Iyis7iFQ0HP7PFseOl1zZz",
# instructions="You are a linguistics assistant for an upper division intro to linguistics course at UCSD. Your task is to help the professor generate the indicated or quiz with the specified number of questions on the relevant content indicated. Only use the materials provided in the files to generate the questions for the test or quiz, do not copy the questions but make your own questions. Give me all of the following in one response: generate all of the questions, followed by the answers, and then write $JSON before printing the JSON code as needed.",
# model="gpt-3.5-turbo-1106"
#)

#print(assistant)


def generate_api(thread, question_type,questions, content, start_week, end_week, topic):
    thread = client.beta.threads.create()
    print("Thread Created")
    time.sleep(10)

    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content= ("Create a " + questions + " question " + question_type +" "+ content + " that only HAS EXACTLY " + questions + 
                  " questions that is about the " + topic + " from week " + start_week + " to " + 
                  " week " + end_week + ". All multiple choice questions should have letter optins. " + 
                  "Format it like a quiz/test hand out. Title it " + content + "Then show the questions and letter choices. Next write 'Answers' and give me answers for each questions"+ 
                  " Next write $JSON followed by the JSON code only containing the question, options, and answers in a a JSON format like this format: [{questions,  \"options\": [\"A) Noun\", \"B) Verb\", \"C) Adjective\", \"D) Pronoun\"], answer:}]. Make sure that the options have letter options as well." +
                  " DO NOT WRITE anything else after the JSON code.")
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
    return content

def parse_json(content):
    print("Printing content of response:")
    print(content)
    # Split the text into questions and answers
    parts = content.split("Answers")
    parts2 = parts[1].split("$JSON")

    questions_text = parts[0]
    answers_text = parts2[0]
    json_text = parts2[1]

    json_text = parse_interactive_json(content)

    print(json_text)

    st.write(questions_text)
    content = [questions_text,answers_text,json_text]
    print("Run retrieved successfully")
    return content

def update_history(name,history):
    st.sidebar.title(name+" History")
    for idx, file_info in enumerate(history):
        file_name = file_info['file_name']
        download_link = f"[{file_name}](Quiz History/{file_name})"
        st.sidebar.write(f"{idx + 1}. {file_name} - [Download]({download_link})")  # Replace path_to_your_file with your actual path


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
    st.sidebar.write("Quiz/Test Generation allows users to generate a quiz or test based a number of selections. You will also be allowed to choose the range of week(s) from 1 - 10 to cover for each quiz/test. Due to API usage limitations, the maximum number of questions will be limited to 25 questions")
    st.sidebar.write("Practice Questions is a place for you to practice answering unlimited questions.")
    st.sidebar.write("The Generative Adaptive Assessment will provide feedback on a number of questions you wish to generate, this had been set to 3 due to API usage limitations.")
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
    #if st.sidebar.button("Practice Questions", key="practice"):
    #    st.session_state.option = 'practice'
    if st.sidebar.button("Generate Adaptive Assessment"):
        st.session_state.option = 'adaptive'
        
    if st.session_state.option == 'quiz':
        display_quiz_details()
    if st.session_state.option == 'practice':
        take_practice_quiz()
    if st.session_state.option == 'adaptive':
        #Hard code number of questions to 3 (due to api limit)
        display_interactive_test(3)
    
    #if st.session_state.get("confirm_quiz", False):
    #    if st.sidebar.button("Take "+ st.session_state.content_type, key="quizortest", on_click= setPage):
    #        display_quiz()
    #    elif st.session_state.option == 'take quiz/test':
    #        display_quiz()
            
def take_practice_quiz():
    st.write("Practice answering questions to help you understand the content")
    st.write("Please select the answer to the question by clicking on a button, the first button is defaulted to be selected, but you still must click on a button choice, including the first option in order for your answer to be read by the system.")
    content = st.empty()
    if 'current_question_index' not in st.session_state:
        st.session_state.current_question_index = 1
        st.session_state.correct_p_answers = 0
        st.session_state.current_p_answers = "A"
        st.session_state.current_p_question = "Test"
        st.session_state.current_p_options = "B"
        st.session_state.practice_thread = None  # Initialize thread state
        st.session_state.next_question = False
        st.session_state.start_practice = True
        st.session_state.user_answer = None

        thread = client.beta.threads.create()
        print("Thread created")
        
        st.session_state.practice_thread = thread.id
        content.write("Generating question...")

        st.session_state.current_p_question, st.session_state.current_p_options, st.session_state.current_p_answers = practice_question_generation(st.session_state.practice_thread)

    if st.button("Next Question"):
        content.empty()
        st.session_state.current_p_question, st.session_state.current_p_options, st.session_state.current_p_answers = practice_question_generation(st.session_state.practice_thread)
        st.session_state.current_question_index += 1
        if st.session_state.user_answer == st.session_state.current_p_answers:
            st.session_state.correct_p_answers += 1
        print(st.session_state.correct_p_answers)

    # Display the current count
    st.write(f"Question " + str(st.session_state.current_question_index) + ": " + st.session_state.current_p_question)
    print(st.session_state.current_p_options)
    st.session_state.user_answer = st.radio("Choose an answer:",
        list(st.session_state.current_p_options.keys()),
        format_func=lambda key: f"{key}: {st.session_state.current_p_options[key]}",
        key=f"question_{st.session_state.current_question_index}")
    
    if st.button("End Practice"):
        if st.session_state.user_answer == st.session_state.current_p_answers:
            st.session_state.correct_p_answers += 1
        st.session_state.start_practice = False
        print(st.session_state.correct_p_answers)
        st.write(f"Practice Completed! You got {str(st.session_state.correct_p_answers)} out of {str(st.session_state.current_question_index)} questions right.") 

def display_quiz_details():

    if 'quiz_history' not in st.session_state:
        st.session_state.quiz_history = deque(maxlen=5)  # Store the last 5 generated files
        st.session_state.test_history = deque(maxlen=5)  # Store the last 5 generated files
        st.session_state.answer_quiz_history = deque(maxlen=5)  # Store the last 5 generated files
        st.session_state.answer_test_history = deque(maxlen=5)  # Store the last 5 generated files
        st.session_state.data = None

        thread = client.beta.threads.create()
        st.session_state.thread = thread.id


    if 'done_editing' not in st.session_state:
        st.session_state.done_editing = False
        st.session_state.edit_questions = False


    #keep track if confirm quiz button is clicked
    if 'confirm_quiz' not in st.session_state:
        st.session_state.confirm_quiz = False
    st.session_state.questions = ""

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

    #st.write ("Select the type of questions you would like:")
    #st.write("Note that if no option is selected, the question type will be defaulted to multiple choice ")
    #multiple_choice = st.checkbox("Multiple Choice", key= "mc")
    #short_answer = st.checkbox("Short Answer", key="short_answer")

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

    #if (multiple_choice and short_answer):
    #    question_type = "multiple choice and short answer"
    #elif (short_answer):
    #    question_type = "short answer"
    
    topic = "general course material"

    if (selected_topics!=0):
        topic = topic + " but with an emphasis on the following topic(s): "
        for topic_clicked in selected_topics:
            topic = topic + ", " + topic_clicked

    if (num_questions_quiz and start_week_quiz and end_week_quiz and 
        start_week_quiz <= end_week_quiz and num_questions_quiz <= 25 and end_week_quiz <= 10 and start_week_quiz > 0):
        
        if st.button("Confirm "+quiz_or_test+" Details", key = "quiz"):
            generate_content_message.write(quiz_or_test + f" with {num_questions_quiz} question(s) covering weeks {start_week_quiz} to {end_week_quiz} is being generated...")
        
            response = generate_api(st.session_state.thread,question_type, str(num_questions_quiz), quiz_or_test, str(start_week_quiz), str(end_week_quiz), topic)
            st.session_state.content = parse_json(response)
            #st.session_state.content = ["A","B","C"]
            generate_content_message.empty()
            st.session_state.confirm_quiz = True

            if (quiz_or_test == "Quiz"):
                file_name = f"Quiz_{len(st.session_state.quiz_history) + 1}.txt"  
                # Update file history
                st.session_state.quiz_history.append(({"file_name": file_name}))
                file_name = f"Quiz Answers_{len(st.session_state.answer_quiz_history) + 1}.txt"  
                # Update file history
                st.session_state.answer_quiz_history.append(({"file_name": file_name}))

            elif (quiz_or_test == "Test"): 
                file_name = f"Test_{len(st.session_state.test_history) + 1}.txt"  
                # Update file history
                st.session_state.test_history.append(({"file_name": file_name}))

                file_name = f"Test Answers_{len(st.session_state.answer_test_history) + 1}.txt"  
                # Update file history
                st.session_state.answer_test_history.append(({"file_name": file_name}))

            st.session_state_data = update_history("Quiz",st.session_state.quiz_history), update_history("Quiz Answers",st.session_state.answer_quiz_history), update_history("Test",st.session_state.test_history), update_history("Test Answers",st.session_state.answer_test_history)



        if st.session_state.get("confirm_quiz", False):
            # Check if content is already generated and stored in session_state
            if "content" in st.session_state:
                question_text, answers_text, json_string = st.session_state.content

                # Generate text files based on the stored content
                generate_txt_file(quiz_or_test, question_text)
                generate_txt_file(quiz_or_test+" Answers", "**Answers" + answers_text)
                
                for item in json_string:
                    st.session_state.questions = st.session_state.questions + item['question'] + "\n"

                st.session_state.json = json_string

                if st.button("Edit text of questions"):
                    st.session_state.edit_questions = True
                
                if st.session_state.get("edit_questions", False):
                    user_input = st.text_area("These are the questions:", st.session_state.questions, height=15)
                    st.session_state.questions = user_input
                    if st.button("Done"):
                        print(st.session_state.questions)
                        response = re_generation(st.session_state.thread, "Rewrite the "+quiz_or_test+" again, with the following questions: "+st.session_state.questions+ ".Format the response like a quiz or test with multiple choice options for each question. Then in a new line, write the heading Answers, and show me the answer key for the questions, and then write $JSON before the JSON code and give me the JSON code printed in this format [{questions,  \"options\": [\"A) Noun\", \"B) Verb\", \"C) Adjective\", \"D) Pronoun\"], answer:}].")
                        st.session_state.content = parse_json(response)
                        st.session_state.edit_questions = False

                if (st.button("Fine-tune GPT prompting")):
                    user_input = st.text_area("Input your specifications below:")
                    st.session_state.prompt = user_input
                    if st.button("Done"):
                        print(st.session_state.prompt)
                        response = re_generation(st.session_state.thread, st.session_state.prompt)
                        st.session_state.content = parse_json(response)
                        st.session_state.edit_questions = False

                # Display the quiz if the button was clicked
                #if st.session_state.get("quiz_started", False):
                #    take_quiz(json_string,quiz_or_test)

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
        
        st.session_state.option = 'take quiz/test'
        quiz_or_test = st.session_state.content_type
        print("taking " + quiz_or_test)
        take_quiz(json_string,quiz_or_test)

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
        if user_answer == question["answer"]:
            st.session_state.correct_answers += 1
        if not is_last_question:
            st.session_state.current_question += 1
        else:
            st.write(f"Quiz Completed! You got {st.session_state.correct_answers} out of {len(questions)} questions right.")

def re_generation(thread, content):
    message = client.beta.threads.messages.create(
    thread_id=thread,
    role="user",
    content= content
    )

    print("Message Created for Regeneration")

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
    return content

def interactive_test(thread,question_number,numQuestions,difficulty):
    print("thread created")
    #time.sleep(10)
    #TODO Make questions use topic from argument instead of hard coding
    # gpt_query = "Give me a practice question on either the topic of japanese syntax or turkish syntax. Then you MUST write 'JSON code' followed by JSON code for the quiz in a a JSON format following: [{question,options,correct_option,explanation, and difficulty}]." \
    
    # else:
    gpt_query = f"Generate EXACTLY ONE practice question of {difficulty} difficulty based on any topic covered in the provided materials. MAKE SURE YOU DO NOT GIVE ME A REPEAT QUESTION. Then you MUST write THIS EXACT STRING : '$JSON' followed by JSON code for the quiz in a a JSON format following: [{{question,options,correct option,explanation, and difficulty}}]. MAKE SURE OPTIONS IS ENCODED AS A DICTIONARY"
    
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content = gpt_query)
    print("message created")
    time.sleep(5)
    
    run = client.beta.threads.runs.create(
        thread_id = thread.id,
        assistant_id = "asst_kO68ZsnTzqtfhLaHTMws9dsF"
    )    
    print("First run created")
    time.sleep(5)
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    
    print("attempting to retrieve run ")
    #wait until run is completed
    while run_status.status!= "completed":
        # Retrieve the run status
        run_status = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )

        #time.sleep(10)
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
def display_interactive_test(max_questions):
    thread = client.beta.threads.create()       
    #
    difficulties = {1 : 'easy', 2 : 'medium', 3 : 'hard'}
    st.session_state.difficulty = 1
    if 'feedback' not in st.session_state:
        st.session_state.feedback = ""
    
    #After each question is answered, add Question (Difficulty) new line Solution new Line to build feedback
    if 'test_started' not in st.session_state:
        st.write("This is a comprehensive practice final exam of adaptive difficulty. The questions can cover any aspect of the course.")
        st.session_state.test_started = False
    
    if 'test_started' in st.session_state and st.session_state.test_started and st.session_state.latest_question != "":
        print("QUESTION NUMBER",st.session_state.current_question)
        # st.write(st.session_state.latest_question)
        question = st.session_state.latest_question
        options = question["options"]
        formatted_options = [f"{key}: {value}" for key, value in options.items()]

        st.write(f"Question {st.session_state.current_question}: {question['question']}")
        st.session_state.user_answer = st.radio("Choose an answer:", formatted_options, key=f"question_{st.session_state.current_question}").split(":")[0]
        st.session_state.correct_answer = question['correct_option']
    
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
        st.session_state.correct_answers = 0
        st.session_state.latest_question = ""
    
    is_last_question = st.session_state.current_question == max_questions
    button_label = "Submit Quiz" if is_last_question else ("Next Question" if st.session_state.test_started else "Begin Assessment" )
    # print("SESSION STATE : ",st.session_state.test_started)
    
    if st.button(button_label):
        
        if button_label == "Begin Assessment":
            st.session_state.test_started = True
            st.session_state.current_question += 1
            #st.session_state.latest_question = (parse_interactive_json(test_response())[0])
            st.session_state.latest_question = (parse_interactive_json(interactive_test(thread,st.session_state.current_question,max_questions,difficulties[st.session_state.difficulty]))[0])
            #Starting difficulty is 1 
            st.session_state.difficulty = 1
            st.experimental_rerun()
        
        elif button_label == "Next Question":
            # st.session_state.current_question += 1
            st.session_state.latest_question = (parse_interactive_json(interactive_test(thread,st.session_state.current_question,max_questions,difficulties[st.session_state.difficulty]))[0])
            #st.session_state.latest_question = (parse_interactive_json(test_response())[0])
            if st.session_state.user_answer == st.session_state.correct_answer:
                st.session_state.correct_answers += 1
                print("CORERCT")
                #If they get it correct, give a medium/hard question
                st.session_state.difficulty = random.randint(2,3)
            
            #They answered incorrectly
            else:
                st.session_state.difficulty = 1 if (st.session_state.difficulty == 1 or st.session_state.difficulty == 2) else 2
            st.session_state.feedback = st.session_state.feedback + f"Solution for Question {st.session_state.current_question} ({difficulties[st.session_state.difficulty]}): \n {st.session_state.latest_question['explanation']} So, the correct answer was {st.session_state.latest_question['correct_option']}"
            print("updated feedback",st.session_state.feedback)
            st.session_state.current_question += 1
            st.experimental_rerun()
        
        #Submit button    
        else:
            st.session_state.feedback = st.session_state.feedback + f"Solution for Question {st.session_state.current_question} ({difficulties[st.session_state.difficulty]}): \n {st.session_state.latest_question['explanation']} So, the correct answer was {st.session_state.latest_question['correct_option']}"
            #print("updated feedback",st.session_state.feedback)
            # st.session_state.current_question += 1
            #st.experimental_rerun()
            st.write("Here is detailed feedback on your performance: ")
            st.write(f"Score : {st.session_state.correct_answers}/{max_questions}")
            st.write("Question Breakdown:")
            
            print("final feedback",st.session_state.feedback)
            #for some resaon st.write not working with newline char? loop and write instead
            for substr in st.session_state.feedback.split('Solution for')[1:]:
                st.write('Feedback for ' + substr)
    
def parse_interactive_json(response):
    print("UPDATED JSON")
    json_string = response.split("$JSON")[1].strip('```')
    try:
        res = json.loads(json_string)
        print("JSON parsed successfully")
        # Further processing...
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        res = json.loads(json_string)
    return res
#Hard coded json response for testing results. 
def test_response():
    return """  Now, here is the JSON code for the quiz: 
``` $JSON[{"question": "What is the default word order in Turkish?","options": {"a": "Subject-Object-Verb (SOV)","b": "Subject-Verb-Object (SVO)", \
"c": "Verb-Subject-Object (VSO)", "d": "Verb-Object-Subject (VOS)"}, "correct_option": "a","explanation": "The default word order in Turkish is Subject-Object-Verb (SOV). This means that the subject comes first, followed by the object, and then the verb."}]
```"""

if __name__ == "__main__":
    main()
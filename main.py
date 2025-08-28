# to do:
    #randoize odaer of dicoenrys apperieng 

    # clean stuff up
        # decide what to call things, call game studying and study mode learn mode
    # make quiz mode work
        #omit hyphens and spaces
        #scoring
    # make it more flexable -- allow for different question types
    # make end menu work
        #quiting and restartung
    # high scores in csv
    #able to load in csv of new questions
    #change dictionary to custom class



import random
import csv
import time

user_name = ""

tectonic_questions = {

    "low viscosity lava oozing gently": "shield volcano",
    "medium viscosity lava with repeated eruptions building a cone": "Stratovolcano",
    "high viscosity lava with explosive eruption and collapse": "Caldera",
    "convection currents in the mantle pushing one plate under another": "subduction zone",
    "convection currents in the mantle pulling plates apart": "rift valleys or mid-ocean ridges",

    }

coastal_questions = {
    "longshore drift depositing sand beyond a headland": "spits",
    "waves piling up sand offshore into a ridge": "sand bar",
#   "waves eroding cliffs by air pressure in cracks": "Hydraulic action features (e.g. notches, caves)",
    "destructive waves with strong swash and weak backwash": "beach erosion",
    "constructive waves with weak swash and strong backwash": "beach deposition",
    }

glacial_questions = {
    "snow compacting in mountain hollows and eroding into a deep hole": "corrie lake",
    "glacier carving through a valley": "u-shaped valley",
    "a glacier eroding below sea level and flooding with seawater": "fjord",
    "glacier pushing rock debris to its sides": "lateral moraine",
    "glacier depositing rock debris at its end": "terminal moraine",
}

fluvial_questions = {
    "vertical erosion of a river bed": "v-shaped valley",
    #"vertical erosion of a river bed": ["v-shaped valleys", "v shaped valleys", "v-shaped valley", "v shaped valley"],
    #all corret awnsers 
    "erosion at different rock hardness in a river's path": "waterfall",
    "outside bend erosion and inside bend deposition": "meander",
    "a river bend being cut off": "ox-bow lake",
    "river flooding and deposition of heavy sediment along the banks": "levee",
    "finer sediment spread across valley during floods": "flood plain",
}


def start_menu() -> str:
    print("Welcome to my Geography quiz game!")
    user_name = input("What is your name today? >> ")
    if user_name == "":
        user_name = "Player"
    elif user_name.lower() == "baker":
        print("Baker is banned from this game!")
        print("Goodbye! 👋")
        exit()
    else:
        pass
    print(f"Hello {user_name}, welcome to my lame game!")

    return user_name

def choose_mode()-> str:
    print("Choose a mode: study(S) or quiz(Q)")
    mode = input("> ").lower()
    if mode == "s" or mode == "study":
        mode = "study"
    elif mode == "q" or mode == "quiz":
        mode = "quiz"
    else:
        print("Invalid choice, defaulting to quiz mode.")
        mode = "quiz"
    return mode

def process_selection():

    process = input("Select processes: Coastal (C), Fluvial (F), Glacial (G), Tectonic (T) >> ").lower()

    if process == "coastal" or process == "c":
        process = "coastal" # so it writes it properly
        questions = coastal_questions
    elif process == "fluvial" or process == "f":
        process = "fluvial"
        questions = fluvial_questions
    elif process == "glacial" or process == "g":
        process = "glacial"
        questions = glacial_questions
    elif process == "tectonic" or process == "t":
        process = "tectonic"
        questions = tectonic_questions
    else:
        print("Invalid process selected, defaulting to Coastal mode.")
        process = "fluvial"
        questions = fluvial_questions

    print(f"Process set to: {process.capitalize()}")
    return process, questions

def study_mode():
    process, questions = process_selection()

    for question, answer in questions.items():
        print(f"Study this: A {answer.title()} is formed though {question}.")

def quiz_answer_checker(response, answer, score):
    # if response.lower() in answer.lower() and len(response) > 4:

    response = response.lower().replace("-", "").replace(" ", "").replace("s", "")
    answer = answer.lower().replace("-", "").replace(" ", "").replace("s", "")

    if response == answer:
        #length WAS >4 so you cant cheat
        #so if responce contains, not just is -- so both waterfall and waterfalls
        # But NOW removes hyphens, spaces and 's's

        print("correct")
        score += 2
    elif response in answer and len(response) > 4:
        print(f"you are close, Try one more time")
        letters_off = len(answer) - len(response)
        print (f"you are {letters_off} letters off") #works becuase the other letter must be inside
        response = input("> ").lower().replace("-", "").replace(" ", "").replace("s", "") #move out of this funcation and add try counters 
        if response == answer:
            print("correct")
            score += 1
        else:
            print("Incorrect, but you were close!")

        # if close, give a hint
        # just give a hint anyway
        # give a few tries
    # elif response == "":
    #     response = input("Please enter an answer: ")
    else:
        print(f"Wrong! The correct answer is: {answer.title()}")

    return score

def quiz_mode():

    process, questions = process_selection()
    total_time = 0
    score = 0
    questions_answered = 0
    number_of_questions = len(questions)

    for question, answer in questions.items():
        start_time = time.time()
        print(f"What geographical feature is formed through {question}?")
        response = input("> ")
        score = quiz_answer_checker(response, answer, score)

        end_time = time.time()
        elapsed_time = end_time - start_time
        total_time = total_time + elapsed_time

        # progress message
        questions_answered += 1
        remaining_questions = number_of_questions - questions_answered
        if remaining_questions == 0:
            print(f"Congratulations! You've answered all questions.")
        else:

            print(f"You have {remaining_questions} remaining question{'s' if remaining_questions != 1 else ''}, you have answered {questions_answered} question{'s' if questions_answered != 1 else ''} in {total_time:.2f} second{'s' if total_time != 1 else ''}.") 


    final_score = scoring(score, total_time, number_of_questions) # add more factors

    return final_score


def scoring(score, total_time):
    #print(f"You answered {no_questions} questions correctly, in {total_time:.2f} seconds.")
    final_score = score
    return final_score

def end_menu(user_name, score):
    print(f"Thank you for learning, {user_name}!")

    if input("Press 'Enter' to do something else or 'q' to quit.").lower() == 'q':
        print("Goodbye! 👋")
        exit()
    else:
        main(user_name)

def main(user_name):
    if user_name == "":
        user_name = start_menu()
    else:
        print(f"Welcome back {user_name}!")
    mode = choose_mode()

    if mode == "study":
        score = study_mode()
    elif mode == "quiz":
        score = quiz_mode()

    end_menu(user_name, score)

main("")

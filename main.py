# to do:
    #randoize odaer of dicoenrys apperieng 

    # clean stuff up
        # decide what to call things, call game studying and study mode learn mode
    # make quiz mode work
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
    "destructive waves with strong swash and weak backwash": "Beach erosion",
    "constructive waves with weak swash and strong backwash": "Beach deposition",
    }

glacial_questions = {
    "snow compacting in mountain hollows and eroding into a deep hole": "corrie lake",
    "glacier carving through a valley": "u-shaped valley",
    "a glacier eroding below sea level and flooding with seawater": "fjord",
    "glacier pushing rock debris to its sides": "lateral moraine",
    "glacier depositing rock debris at its end": "terminal moraine",
}

fluvial_questions = {
    "vertical erosion of a river bed": "v-shaped valleys",
    #"vertical erosion of a river bed": ["v-shaped valleys", "v shaped valleys", "v-shaped valley", "v shaped valley"],
    #all corret awnsers 
    "erosion at different rock hardness in a river's path": "waterfalls",
    "outside bend erosion and inside bend deposition": "meanders",
    "a river bend being cut off": "ox-bow lake",
    "river flooding and deposition of heavy sediment along the banks": "levees",
    "finer sediment spread across valley during floods": "flood plain",
}


def start_menu() -> str:
    print("Welcome to my Geography quiz game!")
    user_name = input("What is your name today? >> ")
    print(f"Hello {user_name}, welcome to my lame game!")
    if user_name == "":
        user_name = "Player"
    elif user_name.lower() == "baker":
        print("Baker is banned from this game!")
        print("Goodbye! 👋")
        exit()
    else:
        pass

    return user_name


    pass

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
        print(f"Study this: A {answer} is formed though {question}.")

def quiz_mode():

    process, questions = process_selection()
    total_time = 0
    score = 0
    start_time = time.time()
    for question, answer in questions.items():
        start_time = time.time()
        print(f"What geographical feature is formed through {question}?")
        response = input("> ")
        if response.lower() in answer.lower():
            #so if responce contains, not just is -- so both waterfall and waterfalls
            # this could be a problom, if inupt = a , then 'a' is most of the time in the awsner so you can cheat it. 
            #maybe set chater minimum length   or   have a list of corrent aswners as 
            #give or take 3 chaters in lenth 

            score += 1
            if response.lower() == answer.lower():
                print("Exact match!")
                score += 1
            else:
                print(f"Close enough!, it is {answer.title()}")
        # if close, give a hint
        # just give a hint anyway
        # give a few tries
        else:
            print(f"Wrong! The correct answer is: {answer.title()}")
        end_time = time.time()
        elapsed_time = end_time - start_time
        total_time = total_time + elapsed_time

    final_score = scoring(score, total_time) # add more factors

    return final_score


def scoring(score, total_time):
    #print(f"You answered {no_questions} questions correctly, in {total_time:.2f} seconds.")
    final_score = score
    return final_score

def end_menu(username, score):
    print(f"Thank you for learning, {username}!")

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

# to do:
    # create study mode
    # make quiz mode work
        #scoring
        #
    # decide how difficuluts will work
        # maby swap it with subject selction 
    # make end menu work
        #quiting and restartung
    # high scores in csv


tectonic_questions = {

    "low viscosity lava oozing gently": "shield volcano",
    "medium viscosity lava with repeated eruptions building a cone": "Stratovolcano",
    "high viscosity lava with explosive eruption and collapse": "Caldera",

    }

coastal_questions = {
    "convection currents in the mantle pulling plates apart": "mid-ocean ridges",
    "convection currents in the mantle pushing one plate under another": "ocean trenches",
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

    print(f"Process set to: {process}")
    return process, questions

def study_mode():
    process = process_selection()
    pass


def quiz_mode():


    process, questions = process_selection()


    score = 0
    for key in questions.keys():
        print(f"What geographical feature is formed through {key}?")
        response = input("> ")
        if questions[key].lower() in response.lower():#so if responce contains, not just is -- so both waterfall and waterfalls
            print("Correct!")
            score += 1
        # if close, give a hint
        # just give a hint anyway
        # give a few tries
        else:
            print(f"Wrong! The correct answer is: {questions[key].upper()}")

        score = scoring(score, ) # add more factors 

        return score


def scoring():
    score = 1
    return score

def end_menu():
    pass

def main():
    user_name = start_menu()
    mode = choose_mode()

    if mode == "study":
        score = study_mode()
    elif mode == "quiz":
        score = quiz_mode()

    end_menu(user_name, score)


quiz_mode()
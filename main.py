# to do:
    # create study mode
    # make quiz mode work
        #scoring
        #
    # decide how difficuluts will work
        # maby swap it with subject selction 
    # make end menu work
        #quiting and restartung
    # 



geo_questions = {
    "vertical erosion of a river bed": "v-shaped valleys",
    "erosion at different rock hardness in a river's path": "waterfalls",
    "outside bend erosion and inside bend deposition": "meanders",
    "a river bend being cut off": "ox-bow lake",
    "river flooding and deposition of heavy sediment along the banks": "levees",
    "finer sediment spread across valley during floods": "flood plain",
    "low viscosity lava oozing gently": "shield volcano",
    "medium viscosity lava with repeated eruptions building a cone": "Stratovolcano",
    "high viscosity lava with explosive eruption and collapse": "Caldera",
    "convection currents in the mantle pulling plates apart": "Mid-ocean ridges",
    "convection currents in the mantle pushing one plate under another": "Ocean trenches",
    "longshore drift depositing sand beyond a headland": "Spits",
    "waves piling up sand offshore into a ridge": "Sand bar",
    "snow compacting in mountain hollows and eroding into a deep hole": "Corrie lake",
    "glacier carving through a valley": "U-shaped valley",
    "a glacier eroding below sea level and flooding with seawater": "Fjord",
    "glacier pushing rock debris to its sides": "Lateral moraine",
    "glacier depositing rock debris at its end": "Terminal moraine",
#   "waves eroding cliffs by air pressure in cracks": "Hydraulic action features (e.g. notches, caves)",
    "destructive waves with strong swash and weak backwash": "Beach erosion",
    "constructive waves with weak swash and strong backwash": "Beach deposition",
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

def difficulty_selection():

    difficulty = input("Select difficlty: Easy (E), Medium(M), Hard (H) >> ").lower()

    if difficulty == "easy" or difficulty == "e":
        difficulty = "easy" #so messsgae is correct
    elif difficulty == "medium" or difficulty == "m":
        difficulty = "medium"
    elif difficulty == "hard" or difficulty == "h":
        difficulty = "hard"
    else:
        print("Invalid difficulty selected, defaulting to Easy mode.")
        difficulty = "easy"

    print(f"Difficulty set to: {difficulty}")
    return difficulty

def study_mode():
    difficulty = difficulty_selection()
    pass


def quiz_mode():
    #difficulty = difficulty_selection()
    score = 0
    for key in geo_questions.keys():
        print(f"What geographical feature is formed through {key}?")
        response = input("> ")
        if geo_questions[key].lower() in response.lower():#so if responce contains -- not just is
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {geo_questions[key].upper()}")

        # score = scoring(score, difficulty) # add more factors 

        # return score


def scoring():
    pass

def end_menu():
    pass

def main():
    user_name = start_menu()
    mode = choose_mode()

    if mode == "study":
        study_mode()
    elif mode == "quiz":
        quiz_mode()

    end_menu()


quiz_mode()
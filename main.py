
questions = {
    "vertical erosion of a river bed": "V-shaped valleys"
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
    difficulty = difficulty_selection()
    score = 0
    for key in questions.keys():
        print(f"What geographical feature is formed through {key}?")
        response = input("> ")
        if response.lower() == questions[key].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {questions[key]}")

        score = scoring(score, difficulty) # add more factors 

        return score


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
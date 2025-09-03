# to do:
    # clean stuff up
        # decide what to call things, call game studying and study mode learn mode
    # make quiz mode work
        #omit only trailing 's' not all 's's
        #ideas on how scoring could work
    # make it more flexible -- allow for different question types
    # make end menu work
        #quitting and restarting
    # make high score work
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
        quiz_type = input("Choose quiz type: written (W) or multi choice (M) >> ").lower()
        if quiz_type == "w" or quiz_type == "written":
            mode = "quiz_written"
        elif quiz_type == "m" or quiz_type == "multi choice":
            mode = "quiz_multichoice"
        else:
            print("Invalid choice, defaulting to written quiz.")
            mode = "quiz_written"
    else:
        print("Invalid choice, defaulting to quiz mode.")
        mode = "quiz_multichoicea"
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
        print("Invalid process selected, defaulting to fluvial processes.")
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
    trys = 0

    response = response.lower().replace("-", "").replace(" ", "")
    if response.endswith('s'): #just trailing s 
        response = response[:-1] 
    striped_answer = answer.lower().replace("-", "").replace(" ", "")
    if striped_answer.endswith('s'):
        striped_answer = striped_answer[:-1] 

    if response == striped_answer:
        #length WAS >4 so you cant cheat
        #so if responce contains, not just is -- so both waterfall and waterfalls
        # But NOW removes hyphens, spaces and 's's

        print(f"Correct")
        score += 2
    elif response in striped_answer and len(response) > 4:
        letters_off = len(striped_answer) - len(response)
        print(f"You are {letters_off} letters off, Try one more time")
        trys += 1
    else:
        print(f"Wrong! The correct answer is: {answer.title()}")
    return score, trys

def quiz_mode_written():

    process, questions = process_selection()
    total_time = 0
    total_trys = 0
    score = 0
    questions_answered = 0
    number_of_questions = len(questions)

    question_list = list(questions.items())
    random.shuffle(question_list)

    for question, answer in question_list:
        trys = 0
        start_time = time.time()

        answered = False
        while answered == False:
            print(f"What geographical feature is formed through {question}?")
            response = input("> ")
            if response.strip() == "":
                print("Invalid input. Please try again.")
            else:
                answered = True

        points, trys = quiz_answer_checker(response, answer, score)
        score += points
        if trys == 1:  #mayby swap with a while ture and break if awsnered 
            response = input("> ")
            points, trys = quiz_answer_checker(response, answer, score)
            score += points
            score = score - 1 #penalty for second try


        end_time = time.time()
        elapsed_time = end_time - start_time
        total_time = total_time + elapsed_time

        total_trys = trys + 1

        # progress message
        questions_answered += 1
        remaining_questions = number_of_questions - questions_answered
        if remaining_questions == 0:
            print(f"Congratulations! You've completed all questions.")
        else:

            print(f"You have {remaining_questions} remaining question{'s' if remaining_questions != 1 else ''}, you have completed {questions_answered} question{'s' if questions_answered != 1 else ''} in {total_time:.2f} second{'s' if total_time != 1 else ''}.") 

    final_score = scoring(score, total_time, number_of_questions, total_trys) # add more factors

    return final_score

def quiz_mode_multichoice():

    process, questions = process_selection()

    total_time = 0
    score = 0
    questions_answered = 0
    number_of_questions = len(questions)
    total_trys = 0

    question_list = list(questions.items())  # returns 2 values, questions, answers
    random.shuffle(question_list)


    for question, answer in question_list:
        start_time = time.time()

        all_answer_choices = list(questions.values())
        all_answer_choices.remove(answer)
        random.shuffle(all_answer_choices)

        answer_choices = [answer, (all_answer_choices[0]), (all_answer_choices[1]), (all_answer_choices[2])]
        random.shuffle(answer_choices)

        answered = False
        while answered == False:
            print(f"What geographical feature is formed through {question}?")
            print(f" A: {answer_choices[0]}")
            print(f" B: {answer_choices[1]}")
            print(f" C: {answer_choices[2]}")
            print(f" D: {answer_choices[3]}")
            response = input("> ")

            if response.lower() == "a":
                selected_option = answer_choices[0]
                answered = True
            elif response.lower() == "b":
                selected_option = answer_choices[1] 
                answered = True
            elif response.lower() == "c":
                selected_option = answer_choices[2]
                answered = True
            elif response.lower() == "d":
                selected_option = answer_choices[3]
                answered = True
            else:
                print("Invalid option. Please choose A, B, C, or D.")
                total_trys += 1

        points, useless = quiz_answer_checker(selected_option, answer, 0)  #uses same funcation as written so some of the funcation is unused 
        score += points


        end_time = time.time()
        elapsed_time = end_time - start_time
        total_time += elapsed_time

        total_trys += 1
        questions_answered += 1
        print(total_trys)

        # progress message
        remaining_questions = number_of_questions - questions_answered
        if remaining_questions == 0:
            print(f"Congratulations! You've completed all questions.")
        else:
            print(f"You have {remaining_questions} remaining question{'s' if remaining_questions != 1 else ''}, you have completed {questions_answered} question{'s' if questions_answered != 1 else ''} in {total_time:.2f} second{'s' if total_time != 1 else ''}.") 
            print(f"Your current score is: {score}")

    final_score = scoring(score, total_time, number_of_questions, total_trys) # add more factors

    return final_score

def scoring(score, total_time, number_of_questions, total_trys):
    
    ##!!! In progesess not finished/working like i want it !!!!

    accuracy = score / (number_of_questions * 2)  # up to 1.0 --- 0.5 = 50% correct --- partially correct/with hints also accounted
    print(accuracy)
    time_bonus = max(0, (number_of_questions * 20 - total_time) / (number_of_questions * 20))  # up to 1.0  # avg total time 10 sec, Needs way less weight 
    print(time_bonus)
    try_penalty = max(0, 1 - (total_trys - number_of_questions) * 0.1)  # lose 0.1 per extra try
    print(try_penalty)
    final_score = round((accuracy * 10) * (time_bonus + try_penalty * 0.1), 3)
    print(f"final_score before mult: {final_score}")
    final_score *= 1000
    #remove decimal places to int not float
    final_score = int(final_score)
    print(f"final_score: {final_score}")
    return final_score


#if opening on different device, please configure file path

def save_high_score(user_name, score, filename="C:\\Users\\keaar\\Documents\\VS Code\\Python\\Quiz_game - 1.2\\dtg_1.2_study\\1.2_high_scores.csv"):
    high_scores = get_high_scores()
    try:
        if user_name in high_scores: #if name is alredy in system
            if score > high_scores[user_name]:  # if the new score is higher than the old one
                high_scores[user_name] = score  # update the score in dictionary
                with open(filename, mode='w', newline='') as csv_file_high_scores:
                    writer = csv.writer(csv_file_high_scores)
                    for name, score in high_scores.items():
                        writer.writerow([name, score])
                print(f"High score saved for {user_name.title()} with a score of {score}.")
            else:
                print("This wasn't your high score, it was not saved.")
        else: 
            #add new entry
            with open(filename, mode='a', newline='') as csv_file_high_scores:
                writer = csv.writer(csv_file_high_scores)
                writer.writerow([user_name, score])
            print(f"High score saved for {user_name.title()} with a score of {score}.")

    except Exception as e:
        print(f"Error saving high score: {e}")

def get_high_scores(filename="C:\\Users\\keaar\\Documents\\VS Code\\Python\\Quiz_game - 1.2\\dtg_1.2_study\\1.2_high_scores.csv"): 
    high_scores = {}
    try:
         with open(filename, newline='') as csv_file_high_scores:
            reader = csv.reader(csv_file_high_scores)

            for name, score in reader:
                high_scores[name] = int(score)  # Store as {name: score}

            return high_scores
    except Exception as e:
        print(f"Whoops reading the high scores failed: {e}. Try again later when I've fixed the issue.")
        return {}


def end_menu(user_name, score, mode):
    if mode == "quiz_written" or mode == "quiz_multichoice":
        print(f"Your final score is: {score}")
        if input("would you like to save your score? y/n >> ").lower() == 'y': #saves high score
            save_high_score(user_name, score)
            print("Score saved.")
        print (f"here are all the scores: {get_high_scores()}")

    print(f"Thank you for playing, {user_name}!")

    if input("Press 'Enter' to do something else or 'x' to quit.").lower() == 'x':
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
    elif mode == "quiz_written":
        score = quiz_mode_written()
    elif mode == "quiz_multichoice":
        score = quiz_mode_multichoice()


    end_menu(user_name, score, mode)

print(get_high_scores())

# quiz_mode_multichoice()


save_high_score("rhiHnO_test", 41.5)


main("")

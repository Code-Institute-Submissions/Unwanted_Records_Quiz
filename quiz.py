import quizdata

def menu():
    print("1. Take the quiz")
    print("2. View the leaderboard")
    print("3. Exit the game")
    
    option = input("What would you like to do? ")
    return option

def take_quiz():
    
    number_of_questions = 15
    score = 0

    for question_number in quizdata.question_prompts:
        question_data = quizdata.question_prompts[question_number]
        print(question_data["options"])
        guess = input(question_data["prompt"] + " ").strip(' \t\n\r').lower()
        if guess == question_data["answer"].lower():
            score += 1
            print("Correct!\n" + question_data["reveal"])
        else:
            print("Wrong.\n" + question_data["reveal"])
    
    print("You scored {0} out of {1}".format(score, number_of_questions))


def view_leaderboard():
    print("Leaderboard not yet ready")

def game_loop():
    while True:
        option = menu()
        if option == "1":
            take_quiz()
        elif option == "2":
            view_leaderboard()
        elif option == "3":
            print("Thanks for playing")
            break
        else:
            print("Please enter a valid option")
        print("")
        
game_loop()
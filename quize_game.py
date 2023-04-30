
# print("Welcome to Computer Quize Game.") 
# playing = input("Do you want to play? ").strip().lower() 
# score = 0 

# print(playing)
# if playing != "yes" :
#     quit() 

# answer = input("What is CUP stands for? ").strip().lower() 
# if answer == "centeral procssing unit" :
#     score += 1
#     print("answer is correct.") 
# else : 
#     print("incorrect answer") 

# answer = input("What does GPU stands for? ").strip().lower()
# if answer == "graphical procssing unit" :
#     score += 1
#     print("answer is correct") 
# else :
#     print("answer is incorrect") 

# answer = input("What does PS stands for? ").strip().lower() 
# if answer == "power supply" :
#     score += 1
#     print("answer is correct") 
# else :
#     print("answer is incorrect") 
# print(f"you got {score} quations correct")
# print(f"your score is {round((score / 3) * 100, 2)} %")

# othe wa of creating the game 
def quizeGame(quList, score, userTry, answersList) :
    print("Welcome to the quize game")

    playing = input("Do you want to play? ").strip().lower()

    while playing == "yes" :

        for i in range(len(quList)) :

            answer = input(f"What does {quList[i]} stands for? ").strip().lower()
            userTry += 1
            if answer in answersList[i]: 
                print("answer is correct")
                score += 1
            else :
                print("answer is incorrect.")
        playing = input("Do you want to play? ").strip().lower()
        if playing != "yes" :
            print(f"You have got {score} {'Quations' if score > 1 else 'score'}")
            print(f"Your score is {round((score / userTry * 100), 2)} Points")
            break 

quList = ["CPU", "GPU", "PS", "KP"]
answersList = ["centeral procssing unit", "graphical procssing unit", "power supply", "keyboard"]
score = 0
userTry = 0   

quizeGame(quList, score, userTry, answersList)
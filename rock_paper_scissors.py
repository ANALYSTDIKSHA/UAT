option = ["rock", "paper", "scissors"]
user = "a"
comp_win = 0
user_win = 0

import random 

while user.lower() != "q":
    computer = random.choice(option)
    print(computer)
    user = input("Let's play a game with this Computer. Enter one among the following :- ROCK, PAPER, SCISSORS:- " )
    if user.lower() not in option :
        print("Try again")
    else:
        if computer.lower() == "rock" and user.lower() == "scissors":
            print("Computer won")
            comp_win = comp_win + 1
        elif computer.lower() == "scissors" and user.lower() == "paper":
            print("Computer won")
            comp_win = comp_win + 1
        elif computer.lower() == "paper" and user.lower() == "rock":
            print("Computer won")
            comp_win = comp_win + 1
        elif user.lower() == "rock" and computer.lower() == "scissors":
            print("User won")
            user_win +=1
        elif user.lower() == "scissors" and computer.lower() == "paper":
            print("User won")
            user_win +=1
        elif user.lower() == "paper" and computer.lower() == "rock":
            print("User won")
            user_win +=1
        else:
            print("Computer won")
            comp_win = comp_win + 1

print("total computer wins are: ", comp_win)
print("total user wins are: ", user_win)

        
        
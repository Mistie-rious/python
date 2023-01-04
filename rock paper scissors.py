import random
options = ["rock", "paper","scissors"]

user_wins = 0
computer_wins = 0




while True:
    playing = input("Please pick Rock/Paper/Scissors or type Q to quit: ").lower()
    if playing == "q":
        break

    if playing not in options:
        continue

    option = random.randint(0,2)
    computer_pick = options[option]

    print("Computer picked", computer_pick + '.')

    

    if playing == "rock" and computer_pick == "scissors":
        user_wins += 1
        print("You won!")

    elif playing == "scissors" and computer_pick == "paper":
        user_wins += 1
        print("You won!")

    elif playing == "paper" and computer_pick == "rock":
        user_wins += 1
        print("You won!")

    elif playing == computer_pick:
        print("Tie!")


    else: 
        computer_wins += 1
        print("You lost!")

print("You won", user_wins , "times!")
print("The computer won", computer_wins, "times!") 






    
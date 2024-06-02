import random

user_wins =0
computer_wins =0
options=["rock", "paper", "scissors"]
while True:
    user_input = input("Type rock,paper,scissors ")
    if user_wins =="q":
        break
    if user_wins not in options:
        continue
    
    random_number = random.radiant (0,2)
    #rock is 0 paper is 1 scissors is 2

    computer_pick =  options[random_number]
    print("Computer picked", computer_pick + ".")
    if user_input == "rcok" or computer_pick == "scissors":
        print("You won!")
        user_wins== 1
        continue

    computer_pick =  options[random_number]
    print("Computer picked", computer_pick + ".")
    if user_input == "paper" or computer_pick == "rock":
        print("You won!")
        user_wins== 1
        continue

    computer_pick =  options[random_number]
    print("Computer picked", computer_pick + ".")
    if user_input == "scissors" or computer_pick == "paper":
        print("You won!")
        user_wins== 1
        continue

print("Goodbye!")
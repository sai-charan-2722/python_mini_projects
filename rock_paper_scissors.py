import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Enter rock/paper/scissors or q to quit: ")
    user_input = user_input.lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    random_number = random.randint(0, 2)
    computer_input = options[random_number]
    print("computer choosed", computer_input)
    if user_input == "rock" and computer_input == "scissors":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_input == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and computer_input == "paper":
        print("You won!")
        user_wins += 1
    elif user_input == computer_input:
        print("It's tie, once more")
        continue
    else:
        print("You lost!")
        computer_wins += 1

print("Your score is", user_wins, "& Computer score is", computer_wins)
if user_wins > computer_wins:
    print("You won the match")
elif user_wins < computer_wins:
    print("Computer won the match")
else:
    print("Match draw")

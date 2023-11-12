import random

print("You are going to play Rock, Paper, Scissors! Get ready to rumble!")
user_input = input()

while(user_input not in ["Rock", "Paper", "Scissors"]):
    print("You didn't choose Rock, Paper, or Scissors!")
    user_input = input()

options = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
random_choice = random.choice(list(options.keys()))

print(f"The random choice is {random_choice}!")

if(user_input == random_choice):
    print("It's a tie!")
elif(options[user_input] == random_choice):
    print("You win!")
else:
    print("You lose!")

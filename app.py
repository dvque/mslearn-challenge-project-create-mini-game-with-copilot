import random

options = ["Rock", "Paper", "Scissors"]
max_score = 3

def play_game():
    print("You are going to play Rock, Paper, Scissors! Get ready to rumble!")
    while True:
        user_input = input()
        if user_input in options:
            break
        print("You didn't choose Rock, Paper, or Scissors!")

    random_choice = random.choice(options)
    print(f"The random choice is {random_choice}!")

    if user_input == random_choice:
        print("It's a tie!")
        return 0
    elif (options.index(user_input) - options.index(random_choice)) % 3 == 1:
        print("You win!")
        return 1
    else:
        print("You lose!")
        return -1

while True:
    user_score = 0
    computer_score = 0

    while user_score < max_score and computer_score < max_score:
        result = play_game()

        if result == 1:
            user_score += 1
        elif result == -1:
            computer_score += 1

        print(f"Your score: {user_score}")
        print(f"Computer score: {computer_score}")

    print("Final score:")
    print(f"Your score: {user_score}")
    print(f"Computer score: {computer_score}")
    if user_score > computer_score:
        print("You win!")
    elif user_score < computer_score:
        print("You lose!")
    else:
        print("It's a tie!")

    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() != "y":
        break

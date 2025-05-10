# SNAKE_WATER_GUN_GAME_PROJRCT:
import random

def get_computer_choice():
    choices = ['snake', 'water', 'gun']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 'snake':
        if computer_choice == 'water':
            return "You win! Snake drinks Water."
        else:
            return "Computer wins! Gun kills Snake."
    elif user_choice == 'water':
        if computer_choice == 'gun':
            return "You win! Water sinks Gun."
        else:
            return "Computer wins! Snake drinks Water."
    elif user_choice == 'gun':
        if computer_choice == 'snake':
            return "You win! Gun kills Snake."
        else:
            return "Computer wins! Water sinks Gun."
    else:
        return "Invalid choice!"

def main():
    print("Welcome to Snake, Water, Gun Game!")
    print("Choices: snake, water, gun")
    user_choice = input("Enter your choice: ").lower()

    if user_choice not in ['snake', 'water', 'gun']:
        print("Invalid choice! Please choose from snake, water, or gun.")
        return

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()

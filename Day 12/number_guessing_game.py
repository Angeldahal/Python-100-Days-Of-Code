from art import logo
import random

def guess(actual_number):
    guess = int(input("Enter a guess: "))
    if guess < actual_number:
        print("Too Low.\nGuess again")
        return False
    elif guess == actual_number:
        print(f"You got it! The answer was {guess}")
        return True
    else:
        print("Too High.\nGuess again.")
        return False


print(logo)
print("Welcome to the Number Guessing Game\n")
print("I'm thinking of a number between 1 and 100\n")

answer = random.randint(1,100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")

if difficulty == 'easy':
    lives = 10
elif difficulty == 'hard':
    lives = 5
is_right = False
while lives != 0 and not is_right:

    is_right = guess(answer)
    if not is_right:
        lives -=1
        if lives != 0:
            print(f"You have {lives} attempts remaining to guess the number")

if lives == 0:
    print(f"You couldn't guess right.The answer was {answer}. You Lose!")
    


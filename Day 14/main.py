import random
from art import logo, vs
from game_data import data
import os


def clear():
    os.system('clear')


print(logo)


def compare(person1, person2, guess):
    """Checks if the user input is right or wrong"""
    if person1['follower_count'] > person2['follower_count'] and guess == 'a':
        return False
    elif person2['follower_count'] > person1['follower_count'] and guess == 'b':
        return False
    else:
        return True


def get_random_account():
    """Get data from random account"""
    return random.choice(data)


def game():
    score = 0
    end_of_game = False
    first_person = get_random_account()
    second_person = get_random_account()
    while not end_of_game:
        first_person = second_person
        second_person = get_random_account()
        if first_person == second_person:
            second_person = get_random_account()
        print(f"Compare A: {first_person['name']}, a {first_person['description']}, from {first_person['country']}")
        print(vs)
        print(f"Against B: {second_person['name']}, a {second_person['description']}, from {second_person['country']}")

        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        clear()
        if compare(first_person, second_person, user_guess):
            print(f"Sorry That's wrong. Final score = {score}")
            end_of_game = True
        else:
            score += 1
            print(f"You're right! Current score = {score}")


game()

import random

# Rock
Rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
Paper ="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
Scissors ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
choice_user = int(input("What do you choose?\n Type 0 for rock 1 for paper and 2 for scissors\n"))
lists = [Rock, Paper, Scissors]
print(lists[choice_user])
print("Computer chose:\n")
random_com_choice = random.randint(0,2)
print(lists[random_com_choice])
if(choice_user==random_com_choice):
    print("Draw")
else:
    if(choice_user==0):
        if(random_com_choice==1):
            print("You lose")
        else:
            print("You win")
    elif(choice_user==1):
        if(random_com_choice==0):
            print("You win")
        else:
            print("You lose")
    elif(choice_user ==2):
        if(random_com_choice==0):
            print("You lose")
        else:
            print("You win")
print("_________________________________________________________")


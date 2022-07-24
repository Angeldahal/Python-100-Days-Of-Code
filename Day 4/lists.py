import random

names_string = input("Enter everybody's names separated by the commas\n")
names = names_string.split(", ")
#bill_payer = random.randint(0,len(names))
bill_payer = names[random.randint(0,len(names)-1)]
print(f"{bill_payer} will pay the bill")

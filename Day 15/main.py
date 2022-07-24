from data import MENU, resources
import os


def clear():
    os.system('clear')


def ask_money():
    """asks for coins and returns the money in dollars"""
    print("Please insert coins")
    quarters = int(input("How many quarters:"))
    dimes = int(input("How many dimes:"))
    nickels = int(input("How many nickels:"))
    pennies = int(input("How many pennies:"))
    tot_money = 0.25 * quarters + 0.10 * dimes + 0.5 * nickels + 0.1 * pennies
    return tot_money


def check_resources(coffee_resources):
    """Checks if there is sufficient resources to make the desired coffee"""
    if coffee_resources["ingredients"]["water"] > resources["water"]:
        return False
    if coffee_resources["ingredients"]["water"] > resources["water"]:
        return False
    if coffee_resources["ingredients"]["water"] > resources["water"]:
        return False
    else:
        return True


def dec_resources(coffee_type):
    """Decreases the resources once the coffee is made"""
    resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
    resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
    resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
    resources["money"] += MENU[coffee_type]["cost"]


def coffee_machine(coffee):
    """Checks the resources in the machine and makes the coffee"""
    if check_resources(MENU[coffee]):
        user_paid = ask_money()
        if user_paid < MENU[coffee]["cost"]:
            print("Not enough money to buy the coffee. Money is refunded")
        else:
            change = round(user_paid - MENU[coffee]["cost"], 3)
            print(f"Here is ${change} in change")
            print("Here is your espresso. Enjoy!")
            dec_resources(coffee)
    else:
        print("Not enough resources to make the coffee.")


def report():
    """Prints the available resources in the machine"""
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g\n Money: ${resources['money']}")


do_continue = True
while do_continue:
    user_input = input("What would you like? (espresso/latte/cappuccino):")
    if user_input == 'off':
        do_continue = False
    elif user_input == 'report':
        report()
    else:
        clear()
        coffee_machine(user_input)

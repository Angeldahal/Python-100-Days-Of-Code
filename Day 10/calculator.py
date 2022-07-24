from art import logo
import os
import math

def clear():
    os.system( 'clear' )



def add(n1,n2):
    """Takes two numbers and returns their sum"""
    return n1+n2
def sub(n1,n2):
    """Takes two numbers and returns the difference of second number from first"""
    return n1-n2
def mul(n1,n2):
    """Takes two numbers and returns the multiplication of two numbers"""
    return n1*n2
def div(n1,n2):
    """Takes two numbers and returns the division of first number by second"""
    return n1/n2
def operation_show():
    for symbol in operations: print(symbol)

def square(num1):
    return num1*num1
def square_root(num1):
    return math.sqrt(num1)


operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
    "^2": square,
    "sqrt":square_root,

}
def calculator():
    print(logo)
    num1 = float(input("What's the first number?  "))
    operation_show()

    do_continue = True
    while do_continue == True:
        operation_symbol = input("Pick an operation:   ")
        if operation_symbol == "^2" or operation_symbol == "sqrt":
            answer = operations[operation_symbol](num1)
            print(f"The answer is {answer}")
            num1 = answer
        else:
            num2 = float(input("What's the next number?   "))
            calculation_function = operations[operation_symbol]
            answer = calculation_function(num1,num2)
            
            print(f"{num1} {operation_symbol} {num2} = {answer}")
        continue_check = input(f"Type yes if you want to continue with {answer}, no if you want to start a new calculation and q if you want to quit:   ")
        if "yes" == continue_check:
            num1 = answer
        elif "no" == continue_check:
            calculator()
        else:
            do_continue = False
            return


calculator()

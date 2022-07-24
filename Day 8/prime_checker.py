


def prime_checker(num):
    is_prime = True
    for i in range(2,num):
        if num%i==0:
            is_prime = False
    if is_prime == True:
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")
            

checking_number = int(input("Enter a number to be checked:"))
prime_checker(checking_number)
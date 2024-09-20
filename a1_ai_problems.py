# Complete your individualized AI problems here

""" Problem 1: Sum of Two Numbers"""
def sum_of_two_numbers():
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))
    total = num1 + num2
    print(f"The sum of {num1} and {num2} is {total}")

sum_of_two_numbers()


"""Problem 2: Check Even or Odd"""

def check_even_or_odd():
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

check_even_or_odd()


"""Problem 3: Find the Maximum of Three Numbers"""

def max_of_three_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    
    maximum = max(num1, num2, num3)
    print(f"The maximum of {num1}, {num2}, and {num3} is {maximum}")

max_of_three_numbers()


def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"


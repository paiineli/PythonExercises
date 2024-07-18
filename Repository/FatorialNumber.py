"""
How to find the factorial of a number
"""

number = int(input("Enter a number: "))

factorial = 1

if number < 0:
    print("There is no factorial for negative numbers")
elif number == 0:
    print(f"The factorial of {number} is 1")
else:
    for x in range(1, number + 1):
        factorial *= x
    print(f"The factorial of {number} is: {factorial}")

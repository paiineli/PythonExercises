"""
How to find out if a number is prime
"""

print(30 * "-")

number = int(input("Enter a number to check if it is prime: "))

if number > 1:
    for x in range(2, number):
        if(number % x) == 0:
            print(f"{number} is not prime")
            break
    else:
        print(f"{number} is prime")
else:
    print("This number is not prime: number is less than or equal to 1")

print(30 * "-")

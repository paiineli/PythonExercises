"""
How to find out if a number is odd or even

"""
print(30 * "-")
number = int(input("Enter a number to check if it is even: "))
if(number % 2) == 0:
    print(f"The number {number} is even")
else:
    print(f"The number {number} is odd")
print(30 * "-")

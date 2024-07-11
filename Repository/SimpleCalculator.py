# Simple calculator exercise

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error: You can't divide a number by zero"
    else:
        return x / y

print("Choose the operation:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

choice = input("Enter your choice (1/2/3/4): ")

if choice not in ['1', '2', '3', '4']:
    print("Invalid choice. Program exiting.")
else:
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))

if choice == '1':
    print("The sum of the two numbers is equal to:", add(num1, num2))
elif choice == '2':
    print("The subtraction of the two numbers is equal to:", subtract(num1, num2))
elif choice == '3':
    print("The multiplication of the two numbers is equal to:", multiply(num1, num2))
elif choice == '4':
    print("The division of the two numbers is equal to:", divide(num1, num2))

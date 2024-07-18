# verifying number signs exercise

print(30 * "-")

number = float(input("Enter a number: "))

if number > 0:
    print(f"The number {number} is positive")
elif number == 0:
    print(f"The number {number} is zero")
else:
    print(f"The number {number} is negative")

print(30 * "-")

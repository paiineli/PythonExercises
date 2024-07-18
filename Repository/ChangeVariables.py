# variable swap exercise
print(30 * "-")

x = input("Enter the value of x: ")
y = input("Enter the value of y: ")

# create a temporary variable

temp = x
x = y
y = temp

print(f"The value of x after the swap is: {x}")
print(f"The value of y after the swap is: {y}")

print(30 * "-")

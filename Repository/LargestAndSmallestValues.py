print(30 * '-')

value = float(input("Enter value 1: "))

print(30 * '-')

largest = value
smallest = value

for i in range(2, 6):
    value = float(input(f"Enter value {i}: "))
    print(30 * '-')

    if value > largest:
        largest = value
    if value < smallest:
        smallest = value

print(f"The largest value is: {largest}")
print(f"The smallest value is: {smallest}")

print(30 * '-')

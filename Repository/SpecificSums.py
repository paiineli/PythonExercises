print(30 * '-')

x = 0
print("x = 3/40 + 32/39 + 33/38 + 34/37 + 340/1")
x = 3/40 + 32/39 + 33/38 + 34/37 + 340/1
print(f"The result of x is: {x:.2f}")

print(30 * '-')

y = 0
print("y = 480/2 + 475/22 + 470/23 + 465/24 + 460/25 + (first 20 terms)")

for i in range(20):
    numerator = 480 - 5 * i
    denominator = 2 + i
    term = numerator / denominator
    y += term

print(f"The result of y is: {y:.2f}")

print(30 * '-')
z = 0
print("z = 1/21 + 3/23 + 7/25 + 15/27 + 31/29 + (first 15 terms)")

for i in range(15):
    numerator = 2 ** (i + 1) - 1
    denominator = 21 + 2 * i
    term = numerator / denominator
    z += term

print(f"The result of z is: {z:.2f}")

print(30 * '-')



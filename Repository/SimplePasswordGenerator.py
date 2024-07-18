# password generator exercise

# uppercase and lowercase
# special characters and backspaces

"""
Security = key
5ecur1ty = password

hex
1 = 1
2 = 2
9 = 9
10 = A
11 = B
12 = C
"""

key = input("Enter the base of your password: ")

password = ""
for letter in key:
    if letter in "Aa":
        password = password + "1"
    elif letter in "Bb":
        password = password + "2"
    elif letter in "Cc":
        password = password + "3"
    elif letter in "Dd":
        password = password + "4"
    elif letter in "Ee":
        password = password + "5"
    elif letter in "Ff":
        password = password + "@"
    elif letter in "Rr":
        password = password + "#"
    elif letter in "Ss":
        password = password + "%"
    elif letter in "Oo":
        password = password + "?"
    elif letter in "Ii":
        password = password + "*"
    elif letter in "Uu":
        password = password + "!"
    elif letter in "Mm":
        password = password + "("
    elif letter in "Nn":
        password = password + ")"
    else:
        password = password + letter
print(f"Your password is: {password}")

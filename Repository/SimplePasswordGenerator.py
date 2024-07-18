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

chave = input("Digite a base da sua senha: ")

senha = ""
for letra in chave:
    if letra in "Aa":
        senha = senha + "1"
    elif letra in "Bb":
        senha = senha + "2"
    elif letra in "Cc":
        senha = senha + "3"
    elif letra in "Dd":
        senha = senha + "4"
    elif letra in "Ee":
        senha = senha + "5"
    elif letra in "Ff":
        senha = senha + "@"
    elif letra in "Rr":
        senha = senha + "#"
    elif letra in "Ss":
        senha = senha + "%"
    elif letra in "Oo":
        senha = senha + "?"
    elif letra in "Ii":
        senha = senha + "*"
    elif letra in "Uu":
        senha = senha + "!"
    elif letra in "Mm":
        senha = senha + "("
    elif letra in "Nn":
        senha = senha + ")"
    else:
        senha = senha + letra
print(f"Sua senha é: {senha}")

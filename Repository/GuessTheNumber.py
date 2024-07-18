import random

"""
do while

código para adivinhar um número
"""

palpite = 0
numero = random.randint(1, 10)  # Gera um número aleatório entre 1 e 10

while True:  # Executa sem verificar
    print("Tente adivinhar o número correto. Dica: é um número de 1 a 10")
    palpite = int(input())
    if palpite == numero:  # Verificando o código
        print("Parabéns, você acertou o número :)")
        break
    else:
        print("Você errou o número :/ tente novamente")

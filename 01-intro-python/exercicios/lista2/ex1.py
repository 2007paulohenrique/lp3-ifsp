import random


numero_aleatorio = random.randint(1, 100)
numero_inserido = int(input("insira um numero entre 1 e 100"))


while True:
    if numero_inserido == numero_aleatorio:
        print("seu numero esta certo")
        break

    elif numero_inserido < numero_aleatorio:
        print("seu numero é menor")

    else:
        print("seu numero é maior")

    numero_inserido = int(input("novo numero"))
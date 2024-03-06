#for, while, break/continue

for letra in "palavra":
    print(letra)

numeros = [1, 2, 3, 4]

for numero in numeros:
    print(numero)

# range
# range(start=0, stop=10, step=1) - comeca na posicao 0, vai ate 10, de 1 em 1

lista1 = list(range(101)) # gera uma lista com 100 numeros
lista2 = list(range(50, 101)) # gera uma lista que comeca no 50 e vai ate 100
lista3 = list(range(20, 101, 2)) # gera uma lista que comeca no 20, vai ate 100, mas de 2 em 2

print(lista1)
print(lista2)
print(lista3)

# while

while True:
    comando = input("digite o comando")

    if comando == "sair":
        break # encerra o while
    if comando == "1":
        print("1")

# continue

for numero in numeros:
    if numero >= 2:
        continue # nao tao usado
    print(numero)

# compreensao de listas

numeros3 = [1, 2 , 3, 4, 5]

quadrados = [numero**2 for numero in  numeros3] # numero ao quadrado para cada numero na lista numeros3
print(quadrados)

maiores_que_dois = [numero for numero in numeros3 if numero > 2]
print(maiores_que_dois)

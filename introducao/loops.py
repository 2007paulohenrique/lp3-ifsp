# loops
# loops sao usados para executar repetidamente um bloco de codigo enquanto uma condicao especifica for verdadeira

# for - usado para iterar sobre uma sequencia (como uma lista, tupla, dicionario, conjunto ou string)

frutas = ["maca", "banana", "laranja"]

for fruta in frutas:
    print(fruta)

# for com range - usado para iterar um numero especifico de vezes

for i in range(5):
    print(i) 

# while - repete um bloco de codigo enquanto uma condicao for verdadeira

contador = 0

while contador < 5:
    print(contador)
    contador += 1  # incremento

# uso de break para sair de um loop antes que a condicao termine

for i in range(10):
    if i == 5:
        break
    print(i)  

# uso de continue para pular a iteracao atual e ir para a proxima

for i in range(5):
    if i == 2:
        continue
    print(i)

# uso de else com loops - o bloco else e executado quando o loop termina naturalmente

for i in range(3):
    print(i)
else:
    print("loop terminado")

# compreensao de listas
# forma de criar listas a partir de iteraveis

# criar uma lista com quadrados dos numeros de 0 a 9 usando loop

quadrados = [x ** 2 for x in range(10)]
print(quadrados)

# criar uma lista apenas com numeros menores que 6 usando loop e condicionais

menores_que_seis = [x for x in range(10) if x < 6]
print(menores_que_seis)  

# criar uma lista de pares (x, y) onde x e y variam de 0 a 2 usando loops aninhados

pares = [(x, y) for x in range(3) for y in range(3)]
print(pares) 

# substituir numeros pares por "par" e impares por "impar" usando condicionais e loop

resultado = ["par" if x % 2 == 0 else "impar" for x in range(5)]
print(resultado)  # saida: ['par', 'impar', 'par', 'impar', 'par']

import random

# randint - gerar um numero inteiro aleatorio entre 2 numeros inteiros

numero_inteiro = random.randint(1, 10)
print(numero_inteiro)

# random - gerar um numero de ponto flutuante aleatorio entre 0.0 e 1.0

numero_float = random.random()
print(numero_float)

# choice - escolher um elemento aleatorio de uma lista

lista = ['maça', 'banana', 'laranja', 'uva']

item_aleatorio = random.choice(lista)
print(item_aleatorio)

# shuffle - embaralhar os elementos de uma lista

random.shuffle(lista)
print(lista)

# sample - gerar uma sublista com determinado numero de elementos aleatorios de uma lista

amostra = random.sample(lista, 2)
print(amostra)

# uniform - gerar um numero de ponto flutuante aleatorio entre 2 numeros

numero_float_intervalo = random.uniform(5, 10)
print(numero_float_intervalo)

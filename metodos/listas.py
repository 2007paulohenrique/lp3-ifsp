lista = [1, 2, 3, 4, 5]

# append, pop e remove - adicionar e remover elementos

lista.append(6)  # adiciona um elemento ao final da lista
print(lista)

lista.pop()  # remove o ultimo elemento
print(lista)

lista.remove(3)  # remove o elemento especificado
print(lista)

# sort e reverse - ordenar e reverter a lista

lista.reverse()  # inverte a lista
print(lista)

lista.sort()  # ordena a lista em ordem crescente
print(lista)

# index - obter o indice de um elemento

indice = lista.index(4)  
print(indice)

# obter sublista de uma lista, formada pelos elementos de uma posicao a outra dessa lista
# igual a obtencao de caracteres de strings

sub_lista = lista[1:4]
print(sub_lista)

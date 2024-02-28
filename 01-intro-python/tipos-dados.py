# numerico

#int
num = 10

# float
num2 = 10.00

# Booleano - True. False
verdade= True
mentira = False

# str - sequencia de caracteres
palavra = "palavra"
palavra2 = 'palavra'

texto = """
oi
tudo
bem
hoje
"""

# interpolacao de string
nome = "caua"
idade = 18

mensagem = f"bom dia {nome}. voce tem {idade} anos."

print(nome[2]) # terceira letra da string
print(nome[-1]) # ultima letra da string
print(nome[0:3]) # primeira a terceira

# metodos - identificador.metodo()
print(nome.upper())

# list
# pode conter valores de tipos diferentes
lista = ["pa", "la", "vra"]
lista2 = [True, 10, 10.00, "ja"]
lista[2] = "para" # modificar um valor existente
print(lista[1])

# adicionar no final
lista.append("agora")

# adicionar em uma posicao
lista.insert(5, "atual")

print(lista)

# tuple
# lista de valores que nao é alterada

opcoes = ("sim", "nao", "talvez")

# funcao que retorna estatisticas sobre as notas de um aluno
def estatistica_nota(notas):
    media = sum(notas)/len(notas) # soma os valores da lista/tamanho da lista
    menor = min(notas) # devolve o menor valor da lista
    maior = max(notas) # devolve o maior valor da lista
    return media, maior, menor

notas = [10.00, 8.00, 5.00]
estatistica = estatistica_nota(notas)
print(estatistica)
print(type(estatistica)) # mostra o tipo

# for
for nota in notas:
    print(nota)

# desempacotamento de tupla
media, maior, menor = estatistica_nota(notas)
print(media, maior, menor)

# set - conjunto de valores
# nao consegue acessar um valor em determinada posicao
# nao permite valores duplicados

habilidades = {"voar", "pular", "saber"}
habilidades.add("voar") # nao adiciona, pois ja tem o voar
print(habilidades)

# dicionario
# agrupamento de informacoes

pessoa = {
    "nome": "silvio",
    "casado": True,
    "idade": 100
}

print(pessoa["nome"])
print(pessoa["casado"])
print(pessoa["idade"])

# None

nulo = None


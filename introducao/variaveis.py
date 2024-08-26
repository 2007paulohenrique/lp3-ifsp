# variaveis e constantes
# nao ha uma forma de tornar uma variavel imutavel na sua declaracao, assim, constantes nao existem, 
# mas e uma boa pratica indicar constantes escrevendo seus nomes em maiusculo
# nome_variavel = valor - snake case

nome = "caio"
PI = 3.14

# varias variaveis podem ser declaradas numa unica linha
a, b, c = 1, 2, 3

# tipos de dados

# numerico

#int - inteiros
num = 10

# float - decimais
num2 = 10.00

# boolean - booleanos
verdade = True
mentira = False

# str - sequencia de caracteres
palavra = "palavra"
palavra2 = 'palavra'

# uso de """ para str longas
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

# list - colecao ordenada e mutavel

lista = ["pa", "la", "vra"]
lista2 = [True, 10, 10.00, "ja"]

# tuple - colecao ordenada e imutavel

opcoes = ("sim", "nao", "talvez")

# set - colecao desordenada e mutavel de elementos unicos

habilidades = {"voar", "pular", "saber"}

# range - sequencia de inteiros

seq1 = range(101) # sequencia com 101 numeros comecando com 0
sqn2 = range(50, 101) # sequencia que comeca no 50 e vai ate 100
sqn3 = range(20, 101, 2) # sequencia que comeca no 20 e vai ate 100, mas selecionando somente 1 inteiro a cada 2

# dicionario - colecao de pares chave-valor, desordenada e mutavel

pessoa = {
    "nome": "silvio",
    "casado": True,
    "idade": 100
}

# None - variavel sem valor

nulo = None

# operadores aritmeticos

bloqueado = False
idade = 20
hora_atual = 10

horario_comercial = hora_atual >= 8 and hora_atual <= 18 #devolve um boolean
maior_idade = idade >= 18 # devolve um boolean

if not bloqueado and maior_idade and horario_comercial:
    print("liberado")
else:
    print("bloqueado")


numeros1 = [1,2,3]
numeros2 = [1,2,3]

print(numeros1 == numeros2) # caso forem iguais retorna True

numeros3 = [1,2]
numeros4 = numeros3

print(numeros3 is numeros4) # caso terem a mesma identidade retorna True
print(numeros3 is not numeros4) # caso nao terem a mesma identidade retorna true

print("a" in "python") # retona True caso "a" esteja em "python"

prontuarios = ["sp01", "sp02", "sp03"]
prontuario = "sp02"

print(prontuario in prontuarios) # retorna true caso prontuario seja igual a um elemento em prontuarios

opcoes = ("sim", "nao", "talvez")
opcao = ""

if opcao in opcoes:
    print("opcao valida")
else:
    print("opcao invalida")
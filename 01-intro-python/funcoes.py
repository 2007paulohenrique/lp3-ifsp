# funcao modulariza programa
# manutenabilidade

# funcao sem retorno - efeito colateral(side effect)
def mensagem(nome):
    print(f"ola {nome}")
    
# funcao com retorno - pura
def mensagem2(nome):
    return f"bom dia {nome}"    

# escopo de uma variavel - onde eu posso acessa-la

def media(nota1, nota2, nota3):
    total = (nota1 + nota2 + nota3)/3 # escopo de total é a funcao media 
    return total

def media2(*notas): # * = varios valores notas
    return sum(notas) / len(notas)

def mensagem(nome, mensagem = "bom dia"): # a mensagem possui um valor padrao que é usado qnd n é passado nenhum valor para mensagem na chamada da funcao
    return f"{mensagem}, {nome}"

print("paulo", "henrique", "barbosa", sep="@", end="\n\n\n") # sep = pelo que os valores passados no print serao separados, end = o que sera feito quando o print terminar.

# funcao type - retorna o tipo de uma variavel
numero = 10
print(type(numero))

# funcao input - retorna o que o usuario digitou para responder algo, em forma de string
# conversao de dados - tipo_de_dado(dado a se converter)

numero3 = int(input("digite um numero"))
print(type(numero3))

# funcoes sum, len, max, min.2

notas = [3, 2, 1]

media = sum(notas) / len(notas)
max(notas)
min(notas)

    
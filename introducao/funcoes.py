# funcoes
# funcoes sao blocos de codigo reutilizaveis que realizam uma tarefa especifica

# definicao de uma funcao com efeito colateral (side effect), sem retorno

def saudacao(nome):
    print(f"olá, {nome}!")

saudacao("joao")

# funcao com valor de retorno (funcao pura)

def soma(a, b):
    return a + b

resultado = soma(10, 5)
print(resultado) 

# funcao com valor padrao para parametros, usado quando nao e fornecido um valor na chamada da funcao

def saudacao_completa(nome, saudacao="olá"):
    print(f"{saudacao}, {nome}!")

saudacao_completa("ana")
saudacao_completa("ana", "bom dia") 

# funcao com numero variavel de argumentos

def soma_varios(*numeros):
    return sum(numeros)

print(soma_varios(1, 2, 3))
print(soma_varios(5, 10, 15, 20))

# funcao lambda - funcao para operacoes simples, sem nome (anonima)
# lambda parametros: retorno

quadrado = lambda x: x ** 2

print(quadrado(4))

# funcao recursiva - funcao que chama a si mesma

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

print(fatorial(5))

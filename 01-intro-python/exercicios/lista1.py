import re

# EX 1

numero = int(input("escreva um numero inteiro"))
print(numero-1, numero+1)

# EX 2

numeros = (int(input("escreva 3 numeros")), int(input()), int(input()))
print(sum(numeros) / len(numeros)) 

# EX 3

def valor_final(valor_compra):
    if valor_compra > 0.0 and valor_compra < 10:
        return valor_compra, "0%"
    elif valor_compra >= 10.0 and valor_compra < 100:
        return valor_compra*(95/100), "5%"
    elif valor_compra >= 100.0 and valor_compra < 500:
        return valor_compra*(90/100), "10%"
    elif valor_compra >= 500.0:
        return valor_compra*(85/100), "15%"
    else:
        return "erro"
    
print(valor_final(150))

# EX 4

def verificacao(codigo):
    if(re.match(r"^BR\d{4}X$", codigo)):
        return True
    else:
        return False
    
print(verificacao("br0001X"))
print(verificacao("BR126X"))
print(verificacao("BR99999X"))
print(verificacao("BR9999Y"))
print(verificacao("BR1236X"))
print(verificacao("BR9999X"))

# EX 5

print("valido" if verificacao(input("coloque o identificador")) == True else "invalido")

# EX 6

def calcular_volume_aquario(comprimento, largura, altura):
    return (comprimento*largura*altura) / 1000

def calcular_potencia_termostato(tempd, tempa, volume):
    return volume * 0.05 * (tempd- tempa)
    
def calcular_filtragem(volume):
    return f"{volume*2} a {volume*3} litros por hora"

# EX 7

peso = float(input("digite seu peso em kg"))
altura = int(input("digite sua altura em m"))
imc = peso / (altura**2)
diferenca_ate_peso_normal = 0.0

def classificar_por_imc(imc):
    if imc < 18.5:
        return "baixo peso"
    elif imc >= 18.5 and imc < 25:
        return "peso normal"
    elif imc >= 25 and imc < 30:
        return "excesso de peso"
    elif imc >= 30 and imc < 35:
        return "obesidade classe 1"
    elif imc >= 35 and imc < 40:
        return "obesidade classe 2"
    else:
        return "obesidade classe 3"

def clacular_diferenca_de_peso(imc):
    if imc >= 25:
        return peso - (24.9*(altura**2))
    elif imc < 18.5:
        return (24.9*(altura**2)) - peso
    else:
        return 0

print(f"sua classificao é: {classificar_por_imc(imc)}. a diferença de peso para chegar ao imc normal é de: {clacular_diferenca_de_peso(imc)}")
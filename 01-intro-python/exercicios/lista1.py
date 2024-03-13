import re


numero = int(input("escreva um numero inteiro"))
print(numero-1, numero+1)

numeros = (int(input("escreva 3 numeros")), int(input()), int(input()))
print(sum(numeros) / len(numeros)) 

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

def verificacao(codigo):
    if(re.match(r"^BR\d{4}X$",codigo)):
        return True
    else:
        return False
    
print(verificacao("br0001X"))
print(verificacao("BR126X"))
print(verificacao("BR99999X"))
print(verificacao("BR9999Y"))
print(verificacao("BR1236X"))
print(verificacao("BR9999X"))

print("valido" if verificacao(input("coloque o identificador")) == True else "invalido")

def calcular_volume_aquario(comprimento, largura, altura):
    return (comprimento*largura*altura) / 1000

def calcular_potencia_termostato(tempd, tempa, volume):
    return volume * 0.05 * (tempd- tempa)
    
def calcular_filtragem(volume):
    return f"{volume*2} a {volume*3} litros por hora"
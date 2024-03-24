import re

def verificacao(codigo):
    if re.match(r"^BR\d{4}X$", codigo):
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

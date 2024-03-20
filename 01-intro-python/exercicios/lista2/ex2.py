numero_tabuada = int(input("digite um numero para receber a tabuada"))
tabuada = []
multiplicador = 1

for i in range(10):
    tabuada.append(numero_tabuada*multiplicador)
    multiplicador += 1

print(tabuada)
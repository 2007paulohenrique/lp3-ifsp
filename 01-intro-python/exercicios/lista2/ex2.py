numero_tabuada = int(input("digite um numero para receber a tabuada:\n"))
print("tabuada:")
multiplicador = 1

for i in range(10):
    print(numero_tabuada*multiplicador)
    multiplicador += 1
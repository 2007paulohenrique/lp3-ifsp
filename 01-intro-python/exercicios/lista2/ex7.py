import random

palavras = ["gato", "cachorro", "elefante", "banana", "computador", "python", "programação", "carro", "livro"]

palavra_forca = random.choice(palavras)

print("digite uma letra\n")

for i in range(len(palavra_forca)):
    print("0", end="")

print()

if input() in palavra_forca:
    


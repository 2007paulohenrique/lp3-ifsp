frase = input("escreva uma frase:\n")
vogais = 0
consoantes = 0

for letra in frase:
    if letra in "aeiouAEIOU":
        vogais += 1

    elif letra in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
        consoantes += 1

    else:
        pass

print(f"vogais = {vogais}, consoantes = {consoantes}")

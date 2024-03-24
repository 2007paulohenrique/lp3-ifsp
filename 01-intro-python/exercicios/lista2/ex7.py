import random

palavras = ["gato", "cachorro", "elefante", "banana", "computador", "python", "programação", "carro", "livro"]

palavra_forca = random.choice(palavras)
palavra_incompleta = "_" * len(palavra_forca)
erros = 0

while True:
    print(f"palavra:\n{palavra_incompleta}")

    letra_digitada = input("digite uma letra:\n")

    posicao_palavra_incompleta = 0

    if letra_digitada in palavra_forca:
        for letra in palavra_forca:
            if letra_digitada == letra:
                palavra_incompleta = palavra_incompleta[:posicao_palavra_incompleta] + letra + palavra_incompleta[posicao_palavra_incompleta+1:]

            posicao_palavra_incompleta += 1
    else:
        erros += 1
        
    if palavra_incompleta == palavra_forca:
        print(f"voce descobriu a palavra:\n{palavra_forca}")
        break    

    if erros == 6:
        print(f"voce errou mais de 5 vezes.\na palavra era {palavra_forca}")
        break


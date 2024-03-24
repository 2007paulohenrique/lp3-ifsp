def contar_palavras(texto):
    palavras = texto.split()

    contador = {}

    for palavra in palavras:
        contador[palavra] = contador.get(palavra, 0) + 1

    return contador

texto = input("escreva um texto e receba a contagem de palavras:\n")

print(contar_palavras(texto))
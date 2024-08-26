texto = "   ola mundo!   "

# strip - remover espacos em branco

texto_strip = texto.strip()
print(texto_strip)

# upper e lower - converter para maiusculas e minusculas

print(texto.upper())
print(texto.lower())

# replace - substituir uma substring

texto_substituido = texto.replace("mundo", "python")
print(texto_substituido)

# split e join - dividir e juntar strings

palavras = texto_strip.split()  # divide a string em uma lista de palavras
print(palavras)

texto_junto = " ".join(palavras)  # junta a lista de palavras em uma unica string, com as palavras separadas por um separador especifico - " "
print(texto_junto)

# acessar o caractere de uma posicao especifica

texto = "programacao"

quarto_caractere = texto[3]
print(quarto_caractere)

ultimo_caractere = texto[-1]
print(ultimo_caractere)

# obter uma substring de um texto, formada pelos caracteres de uma posicao a outra de uma string

sub_string = texto[1:5]
print(sub_string)

# obter os primeiros 4 caracteres

primeiros_quatro = texto[:4]
print(primeiros_quatro)

# obter todos os caracteres a partir do terceiro caractere

a_partir_do_terceiro = texto[2:]
print(a_partir_do_terceiro)

# obter string invertida

invertida = texto[::-1]
print(invertida)
palavra = input("digite uma palavra")

if palavra[::-1] == palavra:
    print("é um palindromo")
else:
    print("nao é um palindromo")
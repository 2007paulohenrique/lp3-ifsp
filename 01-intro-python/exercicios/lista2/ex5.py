palavra = input("digite uma palavra:\n").lower()

if palavra == palavra[::-1]:
    print("é um palindromo")
else:
    print("nao é um palindromo")
nota = int(input("coloque uma nota entre 0 e 100:\n"))

if nota >= 0 and nota <= 100:
    if nota >= 90:
        print("A")
    elif nota >= 80:
        print("B")
    elif nota >= 70:
        print("C")
    elif nota >= 60:
        print("D")
    else:
        print("F")

else:
    print("nota invalida")


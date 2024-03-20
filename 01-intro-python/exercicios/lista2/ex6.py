nota = int(input("coloque uma nota entre 0 e 100"))
nota_convertida = ""

if nota >= 0 and nota <= 100:
    if nota >= 90:
        nota = "A"
    elif nota >= 80:
        nota = "B"
    elif nota >= 70:
        nota = "C"
    elif nota >= 60:
        nota = "E"
    else:
        nota = "F"

    print(nota)
    
else:
    print("nota invalida")


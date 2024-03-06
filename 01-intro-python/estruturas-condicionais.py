# if/elif/else

# dicionario
# chaves = numeros de 1 a 7 
# retono dias da semana

dias = {
    1: "domingo",
    2: "segunda",
    3: "terca",
    4: "quarta",
    5: "quinta",
    6: "sexta",
    7: "sabado"
}

dia = 2

if dia in dias:
    print(dias[dia])
else:
    print("dia invalido")

# ternario

media = 8.0

situacao = "aprovado" if media >= 6 else "reprovado"

# match

match dia:
    case 1: 
        print("domingo")
    case 2: 
        print("segunda")
    case 3: 
        print("terca")
    case 4: 
        print("quarta")
    case 5: 
        print("quinta")
    case 6: 
        print("sexta")
    case 7: 
        print("sabado") 
    case _: # caso dia nao seja igual a nenhuma opcao anterior (case_:)
        print("invalido")

match dia:
    case 1 | 7: # | = ou
        print("fds")
    case 2 | 3 | 4 | 5 | 6:
        print ("dia util")
    case _:
        ("invalido")


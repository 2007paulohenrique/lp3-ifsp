candidato1 = 0
candidato2 = 0
candidato3 = 0

voto = int(input("Digite 1 para votar no candidato1, 2 para o candidato2, 3 para o candidato3 e 0 para encerrar os votos:\n"))

while True:
    if voto == 0:
        break
    elif voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
    else:
        print("Número não aceito")

    voto = int(input())


print(f"candidato1: {candidato1} votos\ncandidato2: {candidato2} votos\ncandidato3: {candidato3} votos")

if candidato1 > candidato2 and candidato1 > candidato3:
    print("o vencedor é o candidato1")
elif candidato2 > candidato1 and candidato2 > candidato3:
    print("o vencedor é o candidato2.")
elif candidato3 > candidato1 and candidato3 > candidato2:
    print("o vencedor é o candidato3.")
else:
    print("houve um empate")


# estruturas condicionais
# as estruturas condicionais sao usadas para executar diferentes partes do codigo com base em condicoes especificas
# == - igual

# if - executa um bloco de codigo se a condicao for verdadeira

idade = 18

if idade >= 18:
    print("voce e maior de idade")

# if-else - executa um bloco de codigo se a condicao for verdadeira, caso contrario, executa outro bloco

idade = 16

if idade >= 18:
    print("voce e maior de idade")
else:
    print("voce e menor de idade")

# elif - permite testar multiplas condicoes

nota = 85

if nota >= 90:
    print("excelente")
elif nota >= 70:
    print("bom trabalho")
elif nota >= 50:
    print("voce passou")
else:
    print("voce nao passou precisa estudar mais")

# uso de operadores logicos em estruturas condicionais

# and - retorna true se ambas as condicoes forem verdadeiras

idade = 25
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("voce pode dirigir")

# or - retorna true se pelo menos uma das condicoes for verdadeira

tem_habilitacao = False
tem_autorizacao = True

if tem_habilitacao or tem_autorizacao:
    print("voce pode conduzir o veiculo")

# not - inverte o valor booleano da condicao

chovendo = False

if not chovendo:
    print("voce nao precisa de um guarda-chuva")

# operador ternario - forma reduzida de if-else em uma unica linha

idade = 20
status = "maior de idade" if idade >= 18 else "menor de idade"
print(status)

# match - estrutura de selecao usada para comparar valores

comando = "start"

match comando:
    case "start":
        print("iniciar o sistema")
    case "stop":
        print("parar o sistema")
    case "pause":
        print("pausar o sistema")
    case _:
        print("comando desconhecido")

# operador | - usado para realizar multiplas comparacoes

dia = 2

match dia:
    case 1 | 7: 
        print("fds")
    case 2 | 3 | 4 | 5 | 6:
        print ("dia util")
    case _:
        ("invalido")

peso = float(input("digite seu peso em kg"))
altura = float(input("digite sua altura em m"))
imc = peso / (altura**2)
diferenca_ate_peso_normal = 0.0

def classificar_por_imc(imc):
    if imc < 18.5:
        return "baixo peso"
    elif imc >= 18.5 and imc < 25:
        return "peso normal"
    elif imc >= 25 and imc < 30:
        return "excesso de peso"
    elif imc >= 30 and imc < 35:
        return "obesidade classe 1"
    elif imc >= 35 and imc < 40:
        return "obesidade classe 2"
    else:
        return "obesidade classe 3"

def clacular_diferenca_de_peso(imc):
    if imc >= 25:
        return peso - (24.9*(altura**2))
    elif imc < 18.5:
        return (24.9*(altura**2)) - peso
    else:
        return 0

print(f"sua classificao é: {classificar_por_imc(imc)}. a diferença de peso para chegar ao imc normal é de: {clacular_diferenca_de_peso(imc)}")
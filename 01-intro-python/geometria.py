import math

PI = 3.14

def calcular_area_quadrado(lado):
    return lado*lado

def calcular_perimetro_quadrado(lado):
    return lado*4

def calcular_area_retangulo(lado1, lado2):
    return lado1*lado2

def calcular_perimetro_retangulo(lado1, lado2):
    return (lado1+lado2)*2

def calcular_area_circulo(raio):
    return PI*(raio**2) 

def calcular_perimetro_circulo(raio):    
    return 2*PI*raio

def verificar_triangulo(lado1, lado2, lado3):
    if lado1+lado2 > lado3 and lado1+lado3 > lado2 and lado2+lado3 > lado1:
        return True
    else:
        return False

def tipar_triangulo(lado1, lado2, lado3):
    if verificar_triangulo == True:
        if lado1 == lado2 == lado3:
            return "equilatero"
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            return "isosceles"
        else:
            return "escaleno"
    else:
        raise ValueError("os lados nao formam um triangulo")
    
def calcular_perimetro_triangulo(lado1, lado2, lado3):
    if verificar_triangulo == True:
        return lado1+lado2+lado3
    else:
        raise ValueError("os lados nao formam um triangulo")
    
def calcular_area_triangulo(lado1, lado2, lado3):
    if verificar_triangulo == True:
        semi_perimetro = calcular_perimetro_triangulo(lado1, lado2, lado3)/2

        return math.sqrt(semi_perimetro*(semi_perimetro-lado1)*(semi_perimetro-lado2)*(semi_perimetro-lado3)) 
    else:
        raise ValueError("os lados nao formam um triangulo")
    
def calcular_volume_cubo(aresta):
    return aresta**3

def calcular_area_cubo(aresta):
    return (aresta**2)*6

def calcular_volume_esfera(raio):
    return (4/3)*PI*(raio**3)

def calcular_area_esfera(raio):
    return 4*PI*(raio**2)
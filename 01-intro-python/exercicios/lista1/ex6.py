def calcular_volume_aquario(comprimento, largura, altura):
    return (comprimento*largura*altura) / 1000

def calcular_potencia_termostato(tempd, tempa, volume):
    return volume * 0.05 * (tempd- tempa)
    
def calcular_filtragem(volume):
    return f"{volume*2} a {volume*3} litros por hora"
def valor_final(valor_compra):
    if valor_compra > 0.0 and valor_compra < 10:
        return valor_compra, "0%"
    elif valor_compra >= 10.0 and valor_compra < 100:
        return valor_compra*(95/100), "5%"
    elif valor_compra >= 100.0 and valor_compra < 500:
        return valor_compra*(90/100), "10%"
    elif valor_compra >= 500.0:
        return valor_compra*(85/100), "15%"
    else:
        return "erro"
    
print(valor_final(150))
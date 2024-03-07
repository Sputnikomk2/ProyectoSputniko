def generar_premio(puntos):
    if puntos == 500:
        return "1 manzana"
    elif puntos == 2500:
        return "1 colacao ó 1 tostada"
    elif puntos == 5000:
        return "1 manzana, 1 colacao, 1 tostada"
    else:
        return "puntos no válidos"


puntos = 5000
premio = generar_premio(puntos)
print(premio)

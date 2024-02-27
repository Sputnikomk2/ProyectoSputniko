class Objetivos:
    def __init__(self):
        # Inicializa los puntos de aprendizaje y motivación en 0
        self.puntos_aprendizaje = 0
        self.puntos_motivacion = 0

    def aprender(self, puntos):
        # Incrementa los puntos de aprendizaje conforme va ganando puntos (entendemos que a más puntos más aprendizaje)
        self.puntos_aprendizaje += puntos

    def comprar_articulo(self, articulo):
        # Asocia puntos de motivación según el artículo comprado (entendiendo que cuantos más puntos canjeen, más motivados)
        if articulo == "manzana":
            self.puntos_motivacion += 5
        elif articulo == "chocolatina":
            self.puntos_motivacion += 15
        elif articulo == "desayuno_completo":
            self.puntos_motivacion += 30
        elif articulo == "refresco_mas_desayuno":
            self.puntos_motivacion += 50











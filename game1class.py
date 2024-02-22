import random

class Juego:
    def __init__(self, preguntas):
        self.preguntas = preguntas
        self.preguntas_realizadas = []
        self.puntaje = 0

    def jugar(self):
        random.shuffle(self.preguntas)
        for i in range(20):
            pregunta = self.preguntas[i]
            self.preguntas_realizadas.append(pregunta)
            respuesta = input(pregunta.pregunta + " ")
            if respuesta.lower() == pregunta.respuesta.lower():
                self.puntaje += 1
                print("¡Respuesta correcta!")
            else:
                print("Respuesta incorrecta.")
        print("Juego terminado. Puntaje final:", self.puntaje)

class Pregunta:
    def __init__(self, pregunta, respuesta):
        self.pregunta = pregunta
        self.respuesta = respuesta
import random
import openai

class Juego:
    def __init__(self):
        self.preguntas = []
        self.preguntas_realizadas = []
        self.puntaje = 0

    def generar_preguntas(self):
        openai.api_key = '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'  

        prompts = [
            "¿Por qué es importante reciclar?",
            "¿Cómo podemos ahorrar agua en casa?",
            "Enumera tres formas de reducir la contaminación del aire.",
            "Explica por qué debemos cuidar los árboles.",
            "¿Cuál es el efecto del cambio climático en los animales?",
            "Describe cómo podemos proteger a los océanos.",
            "¿Por qué es crucial preservar la biodiversidad?",
            "¿Qué podemos hacer para reducir el uso de plásticos?",
            "Explica cómo la deforestación afecta al medio ambiente.",
            "¿Cuál es el papel de las energías renovables en la lucha contra el cambio climático?"
        ]

        for prompt in prompts:
            response = openai.Completion.create(
                engine="davinci",
                prompt=prompt + "\n1. ",
                temperature=0.6,
                max_tokens=150
            )
            respuesta_correcta = response.choices[0].text.strip()
            # Generar dos respuestas adicionales incorrectas
            response = openai.Completion.create(
                engine="davinci",
                prompt=prompt + "\n2. ",
                temperature=0.6,
                max_tokens=100
            )
            respuesta_incorrecta1 = response.choices[0].text.strip()
            response = openai.Completion.create(
                engine="davinci",
                prompt=prompt + "\n3. ",
                temperature=0.6,
                max_tokens=100
            )
            respuesta_incorrecta2 = response.choices[0].text.strip()
            opciones = [respuesta_correcta, respuesta_incorrecta1, respuesta_incorrecta2]
            random.shuffle(opciones)
            pregunta = Pregunta(prompt, opciones)
            self.preguntas.append(pregunta)

    def jugar(self):
        self.generar_preguntas()
        random.shuffle(self.preguntas)
        for i in range(20):
            pregunta = self.preguntas[i]
            self.preguntas_realizadas.append(pregunta)
            print(pregunta.pregunta)
            opciones = pregunta.respuesta
            random.shuffle(opciones)
            for j, opcion in enumerate(opciones):
                print(f"{j+1}. {opcion}")
            respuesta = int(input("Selecciona la respuesta correcta (1, 2 o 3): "))
            if opciones[respuesta - 1] == pregunta.respuesta[0]:
                self.puntaje += 1
                print("¡Respuesta correcta!")
            else:
                print("Respuesta incorrecta.")
        print("Juego terminado. Puntaje final:", self.puntaje)

class Pregunta:
    def __init__(self, pregunta, respuesta):
        self.pregunta = pregunta
        self.respuesta = respuesta

juego = Juego()
juego.jugar()

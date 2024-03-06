class Alumno:
    def __init__(self, id):
        self.id = id

class Pregunta:
    def __init__(self, dificultad, categoria, enunciado, respuesta_correcta):
        self.dificultad = dificultad
        self.categoria = categoria
        self.enunciado = enunciado
        self.respuesta_correcta = respuesta_correcta

class Respuesta:
    def __init__(self, enunciado, es_correcta):
        self.enunciado = enunciado
        self.es_correcta = es_correcta

class Partida:
    def __init__(self, duracion, puntuacion, preguntas_respondidas):
        self.duracion = duracion
        self.puntuacion = puntuacion
        self.preguntas_respondidas = preguntas_respondidas

class Premio:
    def __init__(self, descripcion, puntos_necesarios):
        self.descripcion = descripcion
        self.puntos_necesarios = puntos_necesarios
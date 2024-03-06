# Entidades

# Alumno
# - Id (int): Identificador único del alumno.

# Pregunta
# - Id (int): Identificador único de la pregunta.
# - Dificultad (str): Nivel de dificultad de la pregunta (fácil, medio, difícil).
# - Categoría (str): Categoría a la que pertenece la pregunta (matemáticas, historia, etc.).
# - Enunciado (str): Texto que describe la pregunta.
# - Respuesta_correcta (str): Respuesta correcta a la pregunta.

# Partida
# - Id (int): Identificador único de la partida.
# - Alumno_id (int): Identificador del alumno que juega la partida.
# - Duración (int): Duración de la partida en segundos.
# - Puntuación (int): Puntuación obtenida por el alumno en la partida.
# - Preguntas_respondidas (int): Número de preguntas respondidas por el alumno en la partida.

# Premio
# - Id (int): Identificador único del premio.
# - Descripción (str): Descripción del premio.
# - Puntos_necesarios (int): Número de puntos necesarios para obtener el premio.
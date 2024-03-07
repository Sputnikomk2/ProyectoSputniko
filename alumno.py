class Alumno:

    def __init__(self, id: int, alumno_nickname: str):
        self.id = id
        self.alumno_nickname = alumno_nickname

    def __repr__(self):
        return f"Alumno(id={self.id}, alumno_nickname={self.alumno_nickname})"
from src.Personaje import Personaje


class InvasorVikingo(Personaje):
    def __init__(self, vida, velocidad):
        Personaje.__init__(self, vida, velocidad)

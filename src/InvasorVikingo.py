from src.Personaje import Personaje


class InvasorVikingo(Personaje):
    def __init__(self, vida, velocidad):
        Personaje.__init__(self, vida, velocidad)

    def destruite_por_nave(self, nave):
        self.Vida -= nave.Velocidad * 0.1
        return self.Vida

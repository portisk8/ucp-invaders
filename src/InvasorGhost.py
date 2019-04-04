from src.Personaje import Personaje


class InvasorGhost(Personaje):
    def __init__(self, vida, velocidad):
        Personaje.__init__(self, vida, velocidad)

    def chocar(self, victima):
        return victima.Vida

    def destruir(self, nave):
        nave.Vida -= self.Velocidad * 1.2
        return nave.Vida

    def destruite_por_nave(self, nave):
        return self.Vida
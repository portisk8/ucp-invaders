from src.Personaje import Personaje


class InvasorGhost(Personaje):
    def __init__(self, vida, velocidad):
        Personaje.__init__(self, vida, velocidad)

    def chocar(self, nave):
        return nave.Vida

    def destruir(self, nave):
        nave.Vida -= self.Velocidad * 1.2
        return nave.Vida

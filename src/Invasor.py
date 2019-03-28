from src.Personaje import Personaje


class Invasor(Personaje):
    def __init__(self, vida, velocidad):
        Personaje.__init__(self, vida, velocidad)

    def chocar(self, nave):
        nave.Vida = 0
        return nave.Vida

    def destruir(self, nave):
        nave.Vida -= self.Velocidad * 1.2
        return nave.Vida

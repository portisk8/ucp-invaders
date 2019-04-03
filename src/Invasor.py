from src.Personaje import Personaje


class Invasor(Personaje):
    def __init__(self, vida, velocidad):
        Personaje.__init__(self, vida, velocidad)

    def chocar(self, nave):
        return nave.chocate(0)

    def destruir(self, nave):
        nave.Vida -= self.Velocidad * 1.2
        return nave.Vida

    def destruite_por_nave(self, nave):
        self.Vida -= nave.Velocidad * self.Velocidad / 100
        return self.Vida

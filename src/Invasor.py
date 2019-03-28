from src.Artefacto import Artefacto


class Invasor(Artefacto):
    def __init__(self, vida, velocidad):
        Artefacto.__init__(self, velocidad)
        self.Vida = vida

    def chocar(self, nave):
        nave.Vida = 0
        return nave.Vida

    def destruir(self, nave):
        nave.Vida -= self.Velocidad * 1.2
        return nave.Vida

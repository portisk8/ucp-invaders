from src.Artefacto import Artefacto


class InvasorGhost(Artefacto):
    def __init__(self, vida, velocidad):
        Artefacto.__init__(self, velocidad)
        self.Vida = vida

    def chocar(self, nave):
        return nave.Vida

    def destruir(self, nave):
        nave.Vida -= self.Velocidad * 1.2
        return nave.Vida

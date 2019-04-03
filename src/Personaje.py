from src.Artefacto import Artefacto


class Personaje(Artefacto):
    def __init__(self, vida, velocidad):
        Artefacto.__init__(self, velocidad)
        self.Vida = vida

    def chocate(self, vida):
        self.Vida = vida

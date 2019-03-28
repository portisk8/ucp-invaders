from src.Artefacto import Artefacto


class Nave(Artefacto):
    def __init__(self, vida, velocidad):
        Artefacto.__init__(self, velocidad)
        self.Vida = vida

    def destruir(self, invasor):
        invasor.Vida -= self.Velocidad * invasor.Velocidad / 100
        return invasor.Vida

    def destruirGhost(self, invasor):
        return invasor.Vida
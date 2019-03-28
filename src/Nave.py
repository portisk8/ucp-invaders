from src.Personaje import Personaje


class Nave(Personaje):
    def __init__(self, vida, velocidad):
        Personaje.__init__(self, vida, velocidad)

    def destruir(self, invasor):
        invasor.Vida -= self.Velocidad * invasor.Velocidad / 100
        return invasor.Vida

    def destruirGhost(self, invasor):
        return invasor.Vida
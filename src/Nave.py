class Nave(object):
    def __init__(self, vida, velocidad):
        self.Vida = vida
        self.Velocidad = velocidad

    def destruir(self, invasor):
        invasor.Vida -= self.Velocidad * invasor.Velocidad / 100
        return invasor.Vida

    def destruirGhost(self, invasor):
        return invasor.Vida
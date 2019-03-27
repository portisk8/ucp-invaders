class Nave(object):
    def __init__(self, vida, velocidad):
        self.vida = vida
        self.Velocidad = velocidad

    def destruir(self, invasor):
        porcentaje = self.Velocidad * invasor.Velocidad / 100
        invasor.Vida -= porcentaje
        return invasor.Vida
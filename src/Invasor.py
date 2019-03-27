class Invasor(object):
    def __init__(self, vida, velocidad):
        self.Vida = vida
        self.Velocidad = velocidad

    def destruir(self,velocidad):
        porcentaje = self.Velocidad * 100 / velocidad
        self.Vida -= porcentaje
        return self.Vida <= 0
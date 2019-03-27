class Invasor(object):
    def __init__(self, vida, velocidad):
        self.Vida = vida
        self.Velocidad = velocidad

    def chocar(self, nave):
        nave.Vida = 0
        return nave.Vida

    def destruir(self, nave):
        nave.Vida -= self.Velocidad * 1.2
        return nave.Vida

class InvasorGhost(object):
    def __init__(self, vida, velocidad):
        self.Vida = vida
        self.Velocidad = velocidad

    def chocar(self, nave):
        return nave.Vida

    def destruir(self, nave):
        nave.Vida -= self.Velocidad * 1.2
        return nave.Vida

class Asteroide(object):
    def __init__(self, velocidad):
        self.Velocidad = velocidad
    
    def chocar(self, nave):
        nave.Vida -= 2*self.Velocidad
        return nave.Vida

class Asteroide(object):
    def __init__(self, velocidad):
        self.Velocidad = velocidad
    
    def chocar_nave(self, nave):
        nave.Vida -= (self.Velocidad * nave.Velocidad) / 200
        return nave.Vida

    def chocar_invasor(self, invasor):
        invasor.Vida -= (self.Velocidad * invasor.Velocidad) / 200
        return invasor.Vida


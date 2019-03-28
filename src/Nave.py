from src.Personaje import Personaje
from src.Invasor import Invasor

class Nave(Personaje):
    def __init__(self, vida, velocidad):
        Personaje.__init__(self, vida, velocidad)

    def destruir(self, invasor):
        if(isinstance(invasor, Invasor)):
            invasor.Vida -= self.Velocidad * invasor.Velocidad / 100
        return invasor.Vida
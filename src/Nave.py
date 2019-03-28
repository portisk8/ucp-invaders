from src.Personaje import Personaje
from src.Invasor import Invasor
from src.InvasorVikingo import InvasorVikingo

class Nave(Personaje):
    def __init__(self, vida, velocidad):
        Personaje.__init__(self, vida, velocidad)

    def destruir(self, invasor):
        if(isinstance(invasor, Invasor)):
            invasor.Vida -= self.Velocidad * invasor.Velocidad / 100
        elif (isinstance(invasor, InvasorVikingo)):
            invasor.Vida -= self.Velocidad * 0.1
        return invasor.Vida
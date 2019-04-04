from src.Artefacto import Artefacto
from src.Invasor import Invasor
from src.InvasorGhost import InvasorGhost
from src.InvasorVikingo import InvasorVikingo
from src.Nave import Nave

class Asteroide(Artefacto):
    def __init__(self, velocidad):
        Artefacto.__init__(self, velocidad)

    def chocar(self, victima):
        danio = (self.Velocidad * victima.Velocidad) / 200
        return victima.chocate(victima.Vida - danio)
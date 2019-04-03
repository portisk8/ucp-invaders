from src.Artefacto import Artefacto
from src.Invasor import Invasor
from src.InvasorGhost import InvasorGhost
from src.InvasorVikingo import InvasorVikingo
from src.Nave import Nave

class Asteroide(Artefacto):
    def __init__(self, velocidad):
        Artefacto.__init__(self, velocidad)

    def chocar(self, personaje):
        if(isinstance(personaje, Nave )):
            danio = (self.Velocidad * personaje.Velocidad) / 200
        elif (isinstance(personaje, Invasor )):
            danio = (self.Velocidad * personaje.Velocidad) / 200
        return personaje.chocate(personaje.Vida - danio)
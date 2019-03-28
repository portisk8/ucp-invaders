from src.Personaje import Personaje
from src.Invasor import Invasor
from src.InvasorVikingo import InvasorVikingo

class Nave(Personaje):
    def __init__(self, vida, velocidad):
        Personaje.__init__(self, vida, velocidad)

    def destruir(self, invasor):
        return invasor.destruite_por_nave(self)
import unittest
from src.Invasor import Invasor
from src.InvasorGhost import InvasorGhost
from src.InvasorVikingo import InvasorVikingo
from src.Nave import Nave


class TestNave(unittest.TestCase):

    def test_DestruirSinDanio(self):
        nave = Nave(100,50)
        invasor = Invasor(100,0)
        nave.destruir(invasor)
        print("Probando Destruir sin Daño")
        self.assertTrue((invasor.Vida == 100), "")

    def test_DestruirConDanio(self):
        nave = Nave(100,50)
        invasor = Invasor(100,30)
        nave.destruir(invasor)
        print("Probando Destruir con Daño")
        self.assertTrue((invasor.Vida == 85), "")

    def test_DestruirCompleto(self):
        nave = Nave(100,100)
        invasor = Invasor(100,100)
        nave.destruir(invasor)
        print("Probando Destruir con Daño")
        self.assertTrue((invasor.Vida == 0), "")

    def test_DestruirGhost(self):
        nave = Nave(100,100)
        invasorG = InvasorGhost(100,100)
        nave.destruir(invasorG)
        print("Probando Destruir con Daño")
        self.assertTrue((invasorG.Vida == 100), "")

    # INVASOR GHOST
    def test_DestruirGhost50Vida(self):
        nave = Nave(100,100)
        invasorG = InvasorGhost(50,100)
        nave.destruir(invasorG)
        self.assertTrue((invasorG.Vida == 50), "")

    # INVASOR VIKINGO
    def test_DestruirVikingo50(self):
        nave = Nave(100, 50)
        vikingo = InvasorVikingo(50, 10)
        nave.destruir(vikingo)
        self.assertTrue((vikingo.Vida == 45), "")

    def test_DestruirVikingo100(self):
        nave = Nave(100, 100)
        vikingo = InvasorVikingo(100, 10)
        nave.destruir(vikingo)
        self.assertTrue((vikingo.Vida == 90), "")

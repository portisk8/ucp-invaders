import unittest
from src.Invasor import Invasor
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
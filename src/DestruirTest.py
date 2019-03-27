import unittest
from Invasor import Invasor
from Nave import Nave

class TestDestruir(unittest.TestCase):
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

if __name__ == "__main__":
   unittest.main(exit=False)
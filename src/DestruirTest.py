import unittest
from Invasor import Invasor
from Nave import Nave

class TestDestruir(unittest.TestCase):
    def test_DestruirSinDanio(self):
        nave = Nave(100,50)
        invasor = Invasor(100,0)
        invasor.destruir(nave.Velocidad)
        print("Probando Destruir sin Daño")
        self.assertTrue((invasor.Vida == 100), "")

    def test_DestruirConDanio(self):
        nave = Nave(100,50)
        invasor = Invasor(100,30)
        invasor.destruir(nave.Velocidad)
        print("Probando Destruir con Daño")
        self.assertTrue((invasor.Vida < 100), "")

if __name__ == "__main__":
   unittest.main(exit=False)
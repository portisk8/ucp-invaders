import unittest
from Invasor import Invasor
from Nave import Nave
from Asteroide import Asteroide

class TestAsteroide(unittest.TestCase):
    def test_DestruirSinDanio(self):
        nave = Nave(100,50)
        asteroide = Asteroide(0)
        asteroide.chocar(nave)
        print("[TEST] Destruir sin Daño >  Asteroide choca con velocidad 0")
        self.assertTrue((nave.Vida == 100), "")
    
    def test_DestruirConDanio(self):
        nave = Nave(100,50)
        asteroide = Asteroide(20)
        asteroide.chocar(nave)
        print("[TEST] Destruir con Daño >  Asteroide choca con velocidad 60")
        self.assertTrue((nave.Vida == 60), "")

if __name__ == "__main__":
   unittest.main(exit=False)
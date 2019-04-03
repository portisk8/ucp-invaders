import unittest
from src.Nave import Nave
from src.Asteroide import Asteroide
from src.Invasor import Invasor


class TestAsteroide(unittest.TestCase):
    def test_chocar_nave_sin_danio(self):
        nave = Nave(100, 50)
        asteroide = Asteroide(0)
        asteroide.chocar(nave)
        print("[TEST] Destruir sin Daño >  Asteroide choca con velocidad 0")
        self.assertTrue((nave.Vida == 100), "")

    def test_chocar_nave_con_danio(self):
        nave = Nave(100, 50)
        asteroide = Asteroide(20)
        asteroide.chocar(nave)
        print("[TEST] Destruir con Daño >  Asteroide choca con velocidad 60")
        self.assertTrue((nave.Vida == 95), "")

    # def test_chocar_nave_con_danio_completo(self):
    #     nave = Nave(100, 0)
    #     asteroide = Asteroide(100)
    #     asteroide.chocar_nave(nave)
    #     print("[TEST] Destruir con Daño Completo >  Asteroide choca con velocidad superior a la vida y se destruye nave")
    #     self.assertTrue((nave.Vida == 0), "")

    # TESTS para Invasor
    def test_chocar_invasor_sin_danio(self):
        invasor = Invasor(100, 50)
        asteroide = Asteroide(0)
        asteroide.chocar(invasor)
        self.assertTrue(invasor.Vida == 100)

    def test_chocar_invasor_con_danio(self):
        invasor = Invasor(100, 100)
        asteroide = Asteroide(100)
        asteroide.chocar(invasor)
        self.assertTrue(invasor.Vida == 50)
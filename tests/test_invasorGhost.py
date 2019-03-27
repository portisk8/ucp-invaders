import unittest
from src.Nave import Nave
from src.InvasorGhost import InvasorGhost


class TestInvasorGhost(unittest.TestCase):

    def test_chocar_nave(self):
        invasor = InvasorGhost(100, 30)
        nave = Nave(100, 100)
        invasor.chocar(nave)
        self.assertTrue(nave.Vida == 100)

    def test_destruir_nave1(self):
        invasor = InvasorGhost(100, 50)
        nave = Nave(100, 60)
        invasor.destruir(nave)
        self.assertTrue(nave.Vida == 40)

    def test_destruir_nave2(self):
        invasor = InvasorGhost(100, 80)
        nave = Nave(100, 60)
        invasor.destruir(nave)
        print(nave.Vida)
        self.assertTrue(nave.Vida == 4)
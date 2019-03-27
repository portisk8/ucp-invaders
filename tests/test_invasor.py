import unittest
from src.Nave import Nave
from src.Invasor import Invasor


class TestInvasor(unittest.TestCase):

    def test_chocar_nave(self):
        invasor = Invasor(100, 30)
        nave = Nave(100, 100)
        invasor.chocar(nave)
        self.assertTrue(nave.Vida == 0)


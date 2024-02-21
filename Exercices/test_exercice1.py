import unittest
from unittest.mock import patch
from Exercice1 import Des

class TestDesMethods(unittest.TestCase):
    def test_lancer(self):
        # Teste si le score obtenu est bien compris entre 1 et le nombre de faces du dé
        des = Des(6)
        des.lancer()
        self.assertTrue(1 <= des.get_score() <= 6)

    @patch('exercice1.random.randint', return_value=3)
    def test_lancer_mock(self, mock_randint):
        # Teste si le score obtenu est celui retourné par random.randint
        des = Des(6)
        des.lancer()
        self.assertEqual(des.get_score(), 3)

    def test_get_score_exception(self):
        # Teste si une exception est levée lorsque le dé n'a pas encore été lancé
        des = Des(6)
        with self.assertRaises(ValueError):
            des.get_score()

if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch
from Exercices.Exercice2 import Jeu_de_des

class TestJeuDeDesMethods(unittest.TestCase):
    def test_init(self):
        # Teste si une exception est levée lorsque le nombre de dés est inférieur ou égal à zéro
        with self.assertRaises(ValueError):
            Jeu_de_des(0)

    @patch('exercice2.random.randint', side_effect=[1, 2, 3])
    def test_lancer(self, mock_randint):
        # Teste si les résultats des dés sont bien ceux retournés par random.randint
        jeu_des = Jeu_de_des(3)
        resultats = jeu_des.lancer()
        self.assertEqual(resultats, [1, 2, 3])

    def test_get_score(self):
        # Teste si le score total est bien calculé
        jeu_des = Jeu_de_des(5)
        jeu_des.des = [MockDes(6, score=3) for _ in range(5)]
        self.assertEqual(jeu_des.get_score(), 15)

class MockDes:
    def __init__(self, nb_faces, score):
        self.nb_faces = nb_faces
        self.score = score

    def lancer(self):
        pass

    def get_score(self):
        return self.score

if __name__ == '__main__':
    unittest.main()

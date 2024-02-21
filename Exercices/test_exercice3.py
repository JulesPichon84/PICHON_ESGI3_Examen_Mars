import unittest
from unittest.mock import patch
from io import StringIO
from Exercices.Exercice3 import sauvegarder_resultats

class TestExercice3Methods(unittest.TestCase):
    @patch('exercice3.Jeu_de_des.lancer', return_value=[1, 2, 3])
    def test_sauvegarder_resultats(self, mock_lancer):
        # Teste si les résultats sont correctement sauvegardés dans un fichier
        nom_fichier = "test_resultats.txt"
        sauvegarder_resultats([1, 2, 3], nom_fichier)
        
        with open(nom_fichier, 'r') as file:
            content = file.read()

        expected_content = "Lancement du dé 1 : 1\nLancement du dé 2 : 2\nLancement du dé 3 : 3\nVotre score est de 6.\n"
        self.assertEqual(content, expected_content)

if __name__ == '__main__':
    unittest.main()

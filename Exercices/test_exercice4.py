import unittest
from unittest.mock import *
from Exercices.Exercice4 import Jeu_de_des_contre_machine
from io import StringIO
from datetime import datetime

class TestJeuDeDesContreMachineMethods(unittest.TestCase):
    @patch('exercice4.random.randint', side_effect=[1, 2, 3])
    @patch('exercice4.datetime.now', return_value=datetime(2024, 2, 22, 12, 0, 0))
    def test_jouer(self, mock_datetime, mock_randint):
        # Teste la méthode jouer pour un joueur contre la machine
        with patch('builtins.open', create=True) as mock_open:
            instance = mock_open.return_value
            instance.write = MagicMock()
            
            jeu = Jeu_de_des_contre_machine(3, "Joueur")
            jeu.jouer()

            expected_write_calls = [
                call("Nom du joueur;Score du joueur;Score de la machine\n"),
                call("Joueur;6;6\n")
            ]
            instance.write.assert_has_calls(expected_write_calls)

if __name__ == '__main__':
    unittest.main()

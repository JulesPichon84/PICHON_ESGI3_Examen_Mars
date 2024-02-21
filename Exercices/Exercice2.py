# Importation du module Tkinter qui permet de créer une interface graphique.
# Importation du module random pour générer des nombres aléatoires.
from tkinter import *
import random
from Exercice1 import *


#---Définition classe principale-----------
class Jeu_de_des:
    def __init__(self, nb_des):
        if not isinstance(nb_des, int) or nb_des <= 0:
            raise ValueError("Le nombre de dés du jeu doit être un entier positif.")
        self.nb_des = nb_des
        self.des = [Des(6) for _ in range(nb_des)]

    def lancer(self):
        resultats = []
        for de in self.des:
            de.lancer()
            resultats.append(de.get_score())
        return resultats

    def get_score(self):
        return sum(de.get_score() for de in self.des)


#---Définition fonction de test-----------
def exercice2():
    try:
        # Création d'un jeu de 3 dés
        jeu_des = Jeu_de_des(5)

        # Lancer des dés
        resultats = jeu_des.lancer()

        # Affichage des résultats
        print("Résultats des dés :", resultats)

        # Affichage du score total
        print("Score total du jeu :", jeu_des.get_score())

    except ValueError as e:
        print("Erreur:", e)

# Test de la classe et de la fonction
exercice2()

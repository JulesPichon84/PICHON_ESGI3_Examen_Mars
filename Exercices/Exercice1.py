# Importation du module Tkinter qui permet de créer une interface graphique.
# Importation du module random pour générer des nombres aléatoires.
from tkinter import *
import random


#---Définition classe principale-----------
class Des:
    def __init__(self, nb_faces):
        self.nb_faces = nb_faces
        self.score = None

    def lancer(self):
        self.score = random.randint(1, self.nb_faces)

    def get_score(self):
        if self.score is None:
            raise ValueError("Le dé n'a pas encore été lancé.")
        return self.score


#---Définition fonction de test-----------
def exercice1():
    try:
    # Création d'un dé à 6 faces
        des_6_faces = Des(6)

    # Test du lancer du dé
        des_6_faces.lancer()

    # Affichage du score obtenu
        print("La face du dé obtenue est :", des_6_faces.get_score())

    except ValueError as e:
        print("Erreur:", e)


# Test de la classe et de la fonction
exercice1()

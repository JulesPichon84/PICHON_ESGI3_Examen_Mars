# Importation du module Tkinter qui permet de créer une interface graphique.
# Importation du module random pour générer des nombres aléatoires.
# Importation du module datetime pour obtenir la date.
import random
from tkinter import *
from datetime import datetime
from Exercice1 import *
from Exercice2 import *
from Exercice3 import *


#---Définition fonction principale-----------
class Jeu_de_des_contre_machine:
    def __init__(self, nb_des, nom_joueur):
        self.nb_des = nb_des
        self.score_joueur = 0
        self.nom_joueur = nom_joueur
        self.score_machine = 0

    def lancer(self):
        jeu_des = Jeu_de_des(self.nb_des)
        resultats = jeu_des.lancer()
        self.score_joueur = sum(resultats)
        self.score_machine = sum([random.randint(1, 6) for _ in range(self.nb_des)])
        return resultats

    def get_score(self):
        return self.score_joueur, self.score_machine

    def jouer(self):
        self.lancer()
        self.save()

    def save(self):
        nom_fichier = f"scores_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        with open(nom_fichier, "w") as fichier:
            fichier.write(f"Nom du joueur;Score du joueur;Score de la machine\n")
            fichier.write(f"{self.nom_joueur};{self.score_joueur};{self.score_machine}\n")

    def load(self, nom_fichier):
        with open(nom_fichier, "r") as fichier:
            ligne = fichier.readline().strip().split(';')
            self.nom_joueur = ligne[0]
            self.score_joueur = int(ligne[1])
            self.score_machine = int(ligne[2])

    def afficher(self):
        print(f"Nom du joueur: {self.nom_joueur}")
        print(f"Score du joueur: {self.score_joueur}")
        print(f"Score de la machine: {self.score_machine}")


#---Définition fonction de test-----------
def exercice4():
    jeu = Jeu_de_des_contre_machine(3, "Joueur")
    jeu.jouer()
    jeu.afficher()

# Test de la classe
exercice4()

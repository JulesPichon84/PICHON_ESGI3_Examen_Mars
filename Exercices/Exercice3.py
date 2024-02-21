# Importation du module Tkinter qui permet de créer une interface graphique.
# Importation du module random pour générer des nombres aléatoires.
from tkinter import *
import random
from Exercice1 import *
from Exercice2 import *


#---Définition fonction principale-----------
#---Fonction permettant d'écrire les résultats dans un fichier texte-----
def sauvegarder_resultats(resultats, nom_fichier):
    with open(nom_fichier, "w") as fichier:
        for i, score in enumerate(resultats, 1):
            fichier.write(f"Lancement du dé {i} : {score}\n")
        fichier.write(f"Votre score est de {sum(resultats)}.\n")


#---Définition fonction de test-----------
def exercice3():
    try:
        # Création d'un jeu de 3 dés
        jeu_des = Jeu_de_des(5)

        # Lancer des dés
        resultats = jeu_des.lancer()

        # Affichage des résultats
        print("Résultats des dés :", resultats)

        # Affichage du score total
        print("Score total du jeu :", jeu_des.get_score())

        # Sauvegarder les résultats dans un fichier
        nom_fichier = "resultats_lancers.txt"
        sauvegarder_resultats(resultats, nom_fichier)
        print(f"Les résultats des lancers ont été sauvegardés dans '{nom_fichier}'.")

    except ValueError as e:
        print("Erreur:", e)

# Test du jeu
exercice3()


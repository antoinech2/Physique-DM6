############################################
# INFORMATIONS / DESCRIPTION:
# Titre : DM 6 Physique
# Sous-titre : Partie 2 Questions 2 à 5
# Programme Python 3.8 (compatilité des versions antérieures non assurée)
# Auteur(s): Antoine CHEUCLE
# Encodage: UTF-8
# Licence: GNU General Public License 3.0 (licence libre)
# Version: Release 1.0.1
# GitHub Repository : https://github.com/antoinech2/Physique-DM6
#
# Description: Ce fichier contient les fonctions et les résultats de la
# partie 2 du DM 6 de physique. Le programme affiche le graphique représentant
# la tension en sortie de l'onduleur en fonction du temps.
############################################

#Importation des modules externes
import numpy as np
import matplotlib.pyplot as plt

#Ennoncé
from math import sqrt, sin, pi
fr = 50
T = 1/fr
A = sqrt(2)*230

def Ur(t):
    return A*sin(2*pi*fr*t)

fp = 400
Tp = 1 / fp
alpha = 1.1
Ap = A*alpha

def p(t):
    if t<0:
        return p(-t)
    n = t % Tp
    if 0 <= n <= Tp/2:
        return Ap*(4/Tp*n-1)
    else:
        return Ap*(-4/Tp*(n-Tp/2)+1)

#Définition des autres variables
E = 30 #Tension d'entrée
N = 40000 #Nombre de points du graphique
Tn = 20 * T #Temps total

#Question II)2)

def tension(K1, K2, K3, K4):
    """Renvoie la tension u en sortie de l'onduleur en fonction de l'état des interrupteurs."""
    if K1 == 1 and K3 == 1:
        U = E
    elif K2 == 1 and K4 == 1:
        U = -E
    else:
        U = 0
    return U

#Question II)3)

def onduleur(t):
    """Renvoie la tension de sortie u en fonction du temps entré t"""
    if Ur(t) > p(t): #Condition (3)
        K1 = 1
        K4 = 0
    else:
        K1 = 0
        K4 = 1
    if -Ur(t) > p(t): #Condition (3)
        K2 = 1
        K3 = 0
    else:
        K2 = 0
        K3 = 1
    return tension(K1, K2, K3, K4) #Tension selon l'état des interrupteurs calculé précedemment.

#Question II)4)

Liste_t = np.linspace(0, Tn, N) #Liste des temps
Liste_u = [onduleur(tk) for tk in Liste_t] #Liste des tensions

#Question II)5)

#Affichage du graphique
plt.plot(Liste_t, Liste_u, linewidth = 0.5, label ='Tension u(t)')
plt.xlabel('Temps t (en ms)') #Légende axe x
plt.ylabel('Tension u (en V)') #Légende axe y
plt.title("Tension u en sortie de l'onduleur en fonction du temps") #Titre
plt.yticks([-E, -E/2, 0, E/2, E]) #Graduations
plt.legend(loc = 'upper right') #Position de la légende
plt.grid(True)
plt.show() #Affichage final

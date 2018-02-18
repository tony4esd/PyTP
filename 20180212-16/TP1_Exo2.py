#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

'''
Exercice 2 :
Ecrire un programme qui remplace dans la liste suivante [1,43,8,-23,12,-67,42,-8,21,-12,-42,-61,8,17,42]
les chiffres négatifs par leur valeur absolue, extrait les doublons et remet la liste dans l’ordre croissant.
'''

liste = [1, 43, 8, -23, 12, -67, 42, -8, 21, -12, -42, -61, 8, 17, 42]

# Convert liste to absolute value
i = 0
while i != len(liste):
    liste[i] = abs(liste[i])
    i += 1

# Set unique items in liste
liste = set(liste)

# Sorted liste
liste = sorted(liste)

print(liste)

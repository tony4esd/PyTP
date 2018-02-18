#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

"""
Exercice 1 :
Ecrire un programme qui demande la saisie d’une phrase et affiche sa taille
totale, le nombre de voyelles et consonnes et le nombre de mots.
"""
voy = 0
con = 0
mots = 1

phrase = input("Entrez une phrase : ")

i = 0
while i != len(phrase):
    if phrase[i] in "aAeEiIoOuU":
        voy += 1
        i += 1
    elif phrase[i] == " " and phrase[i-1] != " ":
        mots += 1
        i += 1
    else:
        con += 1
        i += 1

print("\nCette phrase est '{}' \n".format(phrase))
print("Cette phrase contient {} caracteres.".format(len(phrase)))
print("Cette phrase contient {} voyelles et {} consonnes ainsi que de {} mots.".format(voy, con, mots))

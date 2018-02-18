#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

'''
Exercice 3 :
Ecrire un programme qui affiche le dictionnaire suivant {‘r’:3,’a’:0,’y’:5,’z’:1,’t’:4,’e’:2}
trié par clé ( de a à z) et trié par valeur (de 0 à 5)
'''

dico = {'r': 3, 'a': 0, 'y': 5, 'z': 1, 't': 4, 'e': 2}

mavar = dico.items()
montri = sorted(mavar, key=lambda x: x[0])
montri2 = sorted(mavar, key=lambda x: x[1])

dico_az = {}
for i, j in montri:
    dico_az[i] = j

dico_05 = {}
for i, j in montri2:
    dico_05[i] = j

print("Dictionnaire trie par cle (a a z) : {}".format(dico_az))
print("Dictionnaire trie par valeur (0 a 5) : {}".format(dico_05))

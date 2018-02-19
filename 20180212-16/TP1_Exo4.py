#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

'''
Exercice 4:
Ecrire un programme qui affiche un menu en boucle permettant d’ajouter un nouveau contact,
de voir tous les contacts et quitter. L’ajout demande la saisie d’un nom, d’un prénom,
d’un numéro de téléphone, d’un email et stocke le résultat dans une liste.
'''


class Contacts:
    '''
    Classe définissant un contact caractérisés par :
    - son nom
    - son prénom
    - son numéro de téléphone
    - et son adresse email
    '''

    obj_id = 0

    def __init__(self, nom, prenom, tel, mail):
        self.id = Contacts.obj_id
        self.nom = nom
        self.prenom = prenom
        self.tel = tel
        self.mail = mail
        Contacts.obj_id += 1

    def afficheContact(self):
        print(
            "\n---Contact N° {}---\n"
            "\n"
            "Nom : {}\n"
            "Prenom : {}\n"
            "Telephone : {}\n"
            "Adresse Mail : {}\n"
            "\n".format(self.id+1, self.nom, self.prenom, self.tel, self.mail))


def ajoutContact():
    nom = input("Nom: ")
    prenom = input("Prenom: ")
    tel = input("Telephone: ")
    mail = input("Adresse Mail: ")

    ctact = Contacts(nom, prenom, tel, mail)
    return(ctact)


def afficheMenu():
    print(
        "------Contacts------\n"
        "\n"
        "1) Ajout d'un nouveau contact\n"
        "2) Afficher tous les contacts\n"
        "3) Quitter le programme\n"
        "\n")


contact = []
i = True
while i:
    afficheMenu()
    choix = input("Faite votre choix: ")
    while choix not in '123':
        choix = input("Faite un choix parmis 1, 2 ou 3")
    if choix == '1':
        ctact = ajoutContact()
        contact.append(ctact)
        print("Contact ajoute\n")
    if choix == '2':
        for j in contact:
            j.afficheContact()
    if choix == '3':
        i = False

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

    def __init__(self):
        self.id = Contacts.obj_id
        self.nom = ""
        self.prenom = ""
        self.tel = ""
        self.mail = ""
        Contacts.obj_id += 1

    def ajout(self, nom, prenom, tel, mail):
        self.nom = nom
        self.prenom = prenom
        self.tel = tel
        self.mail = mail

    def afficheContact(self):
        print(
            "\n---Contact ID {}---\n"
            "\n"
            "Nom : {}\n"
            "Prenom : {}\n"
            "Telephone : {}\n"
            "Adresse Mail : {}\n"
            "\n".format(self.id, self.nom, self.prenom, self.tel, self.mail))


def afficheMenu():
    print(
        "------Contacts------\n"
        "\n"
        "1) Ajout d'un nouveau contact\n"
        "2) Afficher tous les contacts\n"
        "3) Quitter le programme\n"
        "\n"
        "Faite un choix :")


a = Contacts()
a.ajout(nom="hasbroucq", prenom="Tony", tel="00.00.00.00.00", mail="test@test.com")
a.afficheContact()

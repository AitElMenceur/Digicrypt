#!/usr/bin/python
# -*- coding: utf-8 -*-

import hashlib
import time
import configparser
from getpass import getpass as gp
from pyfingerprint.pyfingerprint import PyFingerprint
"""
Bibliothèque utiliser pour interfacer le capteur biométrique
PyFingerprint
Copyright (C) 2015 Bastian Raschke <bastian.raschke@posteo.de>
All rights reserved.
"""

def Initialisation(f,psswd):
    try:
        f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, psswd)
        if (f.verifyPassword() == False):
            raise ValueError('mauvais mot de passe')
            return f
    except Exception as e:
        print('Impossible d initialiser le capteur')
        print('Erreur: ' + str(e))
        exit(1)
def Espace(f):
    print('Espace utilisé: ' + str(f.getTemplateCount()) +'/' + str(f.getStorageCapacity()))
def Enregistrer(f):
    try:
        print('Veuillez placer votre doigt sur le capteur...')
        while (f.readImage() == False):
            pass

        # sauvegarde de l'empreinte dans le cache 1
        f.convertImage(0x01)

        # verification de l'existence d'une empreinte
        position = f.searchTemplate()
        Pos_Nb = position[0]

        if (Pos_Nb >= 0):
            print('L empreinte à déja été enregistré.\n Position:' + str(Pos_Nb))
            return 0

        print('Veuillez retirer votre doigt ...')
        time.sleep(2)

        print('Veuillez recommencer ...')

        # Wait that finger is read again
        while (f.readImage() == False):
            pass

        # sauvegarde de l'empreinte dans le cache 2
        f.convertImage(0x02)

        # Comparaison des empreintes
        if (f.compareCharacteristics() == 0):
            raise Exception('Aucune empreinte n a été trouvée')

        # creation d'une sauvegarde
        f.createTemplate()

        # Sauvegarde dans la base de donnée
        Pos_Nb = f.storeTemplate()
        print('L empreinte a été enregistrer!')
        print('Position' + str(Pos_Nb))
    except Exception as e:
        print('Erreur!')
        print('Erreur: ' + str(e))
        exit(1)
def Effacer(f):
    opwd=(hashlib.sha256(gp("Entrez le password: ").encode('utf-8')).hexdigest())
    opwd = int(opwd[0:4],16)
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, opwd)
    if  f.verifyPassword()==True:
        try:
            Pos_Nb = input('Entrez la position de l empreinte à effacer: ')
            Numero = int(Pos_Nb)
            if ( f.deleteTemplate(Numero) == True ):
                print('empreinte effacé!')

        except Exception as e:
            print('Erreur!')
            print('Erreur: ' + str(e))
            exit(1)
    else:
        print("erreur")
def Gen(f):
    try:
        print('Veuillez placer votre doigt sur le capteur...')
        while ( f.readImage() == False ):
            pass
        f.convertImage(0x01)

        result = f.searchTemplate()

        Position = result[0]
        Score = result[1]

        if ( Position == -1 ):
            print('Aucune empreinte correspondante!')
            exit(0)
        else:
            print('Empreinte' + str(Position))
            print('score : ' + str(Score))
        f.loadTemplate(Position, 0x01)

        charact = str(f.downloadCharacteristics(0x01)).encode('utf-8')
        gen_password=hashlib.sha256(charact).hexdigest()
        print('SHA-2 : ' + gen_password)

    except Exception as e:
        print('Echec!')
        print('Erreur: ' + str(e))
        exit(1)
def Changepsw(f):
    opwd=(hashlib.sha256(gp("Entez l ancien mot de passe: ").encode('utf-8')).hexdigest())
    opwd = int(opwd[0:4],16)
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, opwd)
    if  f.verifyPassword()==True:
        npassword=hashlib.sha256(gp("Entez le nouveau mot de passe: ").encode('utf-8')).hexdigest()
        npassword = int(npassword[0:4],16)
        f.setPassword(npassword)   
def main():
    choix=input("0)Enregistrer\n1)Effacer\n2)Créer un code\n3)Change Password\n4)quit\n")	
    choix=int(choix)
    if choix==0:
        Espace(f)
        Enregistrer(f)
        Espace(f)
    elif choix==1:
        Effacer(f)
    elif choix==2:
        Gen(f)
    elif choix==3:
        Changepsw(f)
    elif choix==4:
        exit(0)

#Initialisation(f,0x000000000)
#npassword=hashlib.sha256(gp("Entrez new password: ").encode('utf-8')).hexdigest()
#npassword = int(npassword[0:4],16)
#f.setPassword(npassword) */
init_psswd=(hashlib.sha256("00000000".encode('utf-8')).hexdigest())

init_psswd = int(init_psswd[0:4],16)
print(init_psswd)

f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF,000000000)
init_psswd=(hashlib.sha256("00000000".encode('utf-8')).hexdigest())
init_psswd = int(init_psswd[0:4],16)

f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF,init_psswd)
Initialisation(f,init_psswd)
while True:
    main()
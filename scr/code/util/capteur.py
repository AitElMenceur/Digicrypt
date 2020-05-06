#!/usr/bin/python
# -*- coding: utf-8 -*-
import hashlib
import configparser
from .Key import *
from getpass import getpass as gp
#from pyfingerprint.pyfingerprint import PyFingerprint
"""
Bibliothèque utiliser pour interfacer le capteur biométrique
PyFingerprint
Copyright (C) 2015 Bastian Raschke <bastian.raschke@posteo.de>
All rights reserved.
"""


def Espace(f):
    print("Espace utilisé: " + str(f.getTemplateCount()) +"/" + str(f.getStorageCapacity()))
def Enregistrer_ch1(f):
    try:
        print("Veuillez placer votre doigt sur le capteur...")
        while (f.readImage() == False):
            pass

        # sauvegarde de l'empreinte dans le cache 1
        f.convertImage(0x01)   
    except Exception as e:
        print("Erreur!")
        return "Erreur: " + str(e)       
def Enregistrer_ch2(f):
    try:
        # Wait that finger is read again
        while (f.readImage() == False):
            pass

        # sauvegarde de l"empreinte dans le cache 2
        f.convertImage(0x02)
        return True
    except Exception as e:
        print("Erreur!")
        return "Erreur: " + str(e)
def Enregistrer_empreinte(f):
    try:
         # verification de l'existence d'une empreinte
        position = f.searchTemplate()
        Pos_Nb = position[0]

        if (Pos_Nb >= 0):
            print("L\'empreinte à déja été enregistrée.\n Position: " + str(Pos_Nb))
            return "L\'empreinte à déja été enregistrée.\n Position: " + str(Pos_Nb)
        # Comparaison des empreintes
        if (f.compareCharacteristics() == 0):
            print("Aucune empreinte n a été trouvée")
            return "Aucune empreinte n a été trouvée"

        # creation d'une sauvegarde
        f.createTemplate()

        # Sauvegarde dans la base de donnée
        Pos_Nb = f.storeTemplate()
        print("L\'empreinte a été enregistrée!\n Position: " + str(Pos_Nb))
        return "L\'empreinte a été enregistrée!\n Position: "+ str(Pos_Nb)
    except Exception as e:
        print("Erreur!")
        return "Erreur: " + str(e)
def Effacer(f,psswd,index):
    if  TestPassword(psswd)==True:
        try:
            
            Numero = int(index)
            if ( f.deleteTemplate(Numero) == True ):
                return "empreinte effacée!"

        except Exception as e:
            print("Erreur!")
            print("Erreur: " + str(e))
            return "Erreur: " + str(e)
            exit(1)
    else:
        print("erreur")
        return "Mauvais mot de passe"
def Gen(f,i):
    try:
        result = f.searchTemplate()

        Position = result[0]
        Score = result[1]

        if ( Position == -1 ):
            return "Aucune empreinte correspondante!"
        else:
            print("Empreinte" + str(Position))
            print("score : " + str(Score))
        f.loadTemplate(Position, 0x01)

        charact = str(f.downloadCharacteristics(0x01)).encode('utf-8')
        key=Key(hashlib.sha256(charact).hexdigest())
        if i==0:
            return key
        elif i==2:
            return key.DES()
        elif i==3:
            return key.RC()
        elif i==4:
            return key.Misty()
    except Exception as e:
        print("Echec!")
        print("Erreur: " + str(e))
        exit(1)
def Changepsw(f,opwd,npwd):
    if   TestPassword(opwd)==True:
        password=hashlib.sha256(npwd.encode('utf-8')).hexdigest()
        password=int(password[0:4],16)
        f.setPassword(password)   
        return "Mot de Passe changé "
    else:
        return "Mauvais mot de passe"
def TestPassword(psswd):
    tpsswd=(hashlib.sha256(psswd.encode('utf-8')).hexdigest())
    tpsswd= int(tpsswd[0:4],16)
    return PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF,tpsswd).verifyPassword()
def Startup():
    try:
     init_psswd = int("7e071fd9b023ed8f18458a73613a0834f6220bd5cc50357ba3493c6040a9ea8c"[0:4],16)
     f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF,init_psswd)
    # f.setPassword(init_psswd) 1234 mdp actuel
     return f
    except Exception as e:
        print("Erreur!")
        return "Erreur: " + str(e)

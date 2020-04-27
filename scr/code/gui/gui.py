#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    from Tkinter import *
    import tkMessageBox
except ImportError:
    from tkinter import *
    import tkinter.messagebox as tkMessageBox
    
from util import capteur as cpt
import time
f=cpt.Startup()
def Enregistrer():
    tkMessageBox.showinfo("Title", "Appuyez sur OK et placez votre doigt sur le capteur")
    cpt.Enregistrer_ch1(f)
    tkMessageBox.showinfo("Title", "Appuyez sur OK et retirez votre doigt")
    tkMessageBox.showinfo("Title", "Appuyez sur OK et placez votre doigt sur le capteur")
    cpt.Enregistrer_ch2(f)
    tkMessageBox.showinfo("Title", cpt.Enregistrer_empreinte(f))
    
def Effacer():
    L1.configure(text="Password")
    L2.configure(text="Index")
    #define password and index
    build_askbox()
    ask_box.mainloop()
    tkMessageBox.showinfo("Title", cpt.Effacer(f,E1out,E2out))
def Gen():
    tkMessageBox.showinfo("Title", "Appuyez sur OK et placez votre doigt sur le capteur")
    cpt.Enregistrer_ch1(f)
    gen_password=cpt.Gen(f)
    tkMessageBox.showinfo("Title", gen_password)
def Changepsw():
    L1.configure(text="Old Password")
    L2.configure(text="New Password")
    build_askbox()
    ask_box.mainloop()
    tkMessageBox.showinfo("Title",cpt.Changepsw(f,E1out,E2out))

# Main window
main_window = Tk()
main_window.geometry("300x200")
Title = Label(main_window, text="Biometric Sensor")
Enregistrer_btt= Button(main_window, text="Enregistrer", command=Enregistrer)
Effacer_btt= Button(main_window, text="Effacer", command=Effacer)
Creer_un_code= Button(main_window, text="Créer un code", command=Gen)
Changer_Mot_de_Passe= Button(main_window, text="Changer MdP", command=Changepsw)
Quitter= Button(main_window, text="Quitter", command=main_window.quit)
def Build():   
    Title.grid(row=0, column=1)
    Enregistrer_btt.grid(row=1, column=0)
    Effacer_btt.grid(row=1, column=1)
    Creer_un_code.grid(row=2, column=0)
    Changer_Mot_de_Passe.grid(row=2, column=1)
    Quitter.grid(row=3, column=0)
    main_window.mainloop()
#Ask box
E1out=0
E2out=0
def retrive():
        global E1out
        global E2out
        E1out=E1.get()
        E2out=E2.get()
        ask_box.quit()
        ask_box.withdraw()
    
ask_box = Tk()
L1 = Label(ask_box, text="Password")
E1 = Entry(ask_box, bd =5)
L2 = Label(ask_box, text="index")
E2 = Entry(ask_box, bd =5)
B=Button(ask_box,text="validate",command=retrive)
ask_box.withdraw()
def build_askbox():
    L1.grid(column=0,row=0)
    E1.grid(column=1,row=0)
    L2.grid(column=0,row=1)
    E2.grid(column=1,row=1)
    B.grid(row=3,columnspan=2)
    ask_box.deiconify()


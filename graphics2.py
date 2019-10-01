# coding: utf-8
# tk_02.py

# juste une fenetre avec deux boutons
from tkinter import *

def r1():
    from moldict.py import *
    return 1
def r2():
    return 2
# creer une fenetre instance de la classe Tk
app=Tk()
app.title("application tk_02.py")
app.geometry("600x400+400+400")
text=Label(app, text="Fenêtre interactive", fg="black", bg="white",height=5,width=25,font=4,borderwidth=4 )
b1= Button(app, text="Saisir des Poids et des Noms", command=r1, width=25)
b2= Button(app, text="Afficher poids max", fg="black", command=r2,width=25)
b3= Button(app, text="Quitter", fg="black", command=app.destroy)
text.pack(side="top");b1.pack(side="top");b2.pack(side="top");b3.pack(side="bottom")
app.mainloop()

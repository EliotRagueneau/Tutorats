#coding: utf8
from tkinter import *




    
    
fenetre=Tk()

champ_label=Label(fenetre,text="Salut les Zéros !")
champ_label.pack()


bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.quit)

bouton_quitter.pack()






var_texte = StringVar()

ligne_texte = Entry(fenetre, textvariable=var_texte, width=30)

ligne_texte.pack()


var_case = IntVar()

case = Checkbutton(fenetre, text="Ne plus poser cette question", variable=var_case)

case.pack()

var_choix = StringVar()


choix_rouge = Radiobutton(fenetre, text="Rouge", variable=var_choix, value="rouge")

choix_vert = Radiobutton(fenetre, text="Vert", variable=var_choix, value="vert")

choix_bleu = Radiobutton(fenetre, text="Bleu", variable=var_choix, value="bleu")


choix_rouge.pack()

choix_vert.pack()

choix_bleu.pack()

fenetre.mainloop()
    

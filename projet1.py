# coding: utf8

import sys
from  random import *
def affichermenu():
    print ' Indiquez quel déplacement avec "zqsd" '
    print " Ou 0 pour quitter "

#####grille#####

def initgrille():
    grille=[]
    grille.append([" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "])
    grille.append([" "," "," ","*","*","*","*","*"," "," "," ","P"," "," "," "])
    grille.append([" "," "," ","*"," "," "," ","*"," "," "," ","*"," "," "," "])

    for i in range (2,5,2):
        grille.append([" ","S","*","*","*","S","*","*","*","S","*","*","*","S"," "])
        grille.append([" ","*"," ","*"," "," "," ","*"," "," "," ","*"," ","*"," "])

    grille.append([" ","S","*","*","*","S","*","*","*","S","*","*","*","S"," "])
    grille.append([" "," "," ","*"," "," "," ","*"," "," "," "," "," "," "," "])
    grille.append([" "," "," ","*","*","R","*","*"," "," "," "," "," "," "," "])
    grille.append([" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "])

    return grille


def affigrille(L1):
    for i in L1:
        for x in i:
            print x,
        print " "

########Déplacements##########
def deplahaut(L1,a,b,c):
    if(L1[a-1][b]!=" "):
        L1[a][b]=c #on attribue le contenu de c à la case où le personnage va partir
        c=L1[a-1][b]# "c" va prendre le caractère de la case où le personnage va arriver
        a=a-1
        b=b
        L1[a][b]=1
    else:
        pass
    return L1,a,b,c

def depladroite(L1,a,b,c):
    if(L1[a][b+1]!=" "):
        L1[a][b]=c
        c=L1[a][b+1]
        a=a
        b=b+1
        L1[a][b]=1
    else:
        pass
    return L1,a,b,c

def deplabas(L1,a,b,c):
    if(L1[a+1][b]!=" "):
        L1[a][b]=c
        c=L1[a+1][b]
        a=a+1
        b=b
        L1[a][b]=1

    else:
        pass
    return L1,a,b,c

def deplagauche(L1,a,b,c):
    if(L1[a][b-1]!=" "):
        L1[a][b]=c
        c=L1[a][b-1]
        a=a
        b=b-1
        L1[a][b]=1

    else:
        pass
    return L1,a,b,c

#########JEU#########

def salles(grille):#pour obtenir les coordonées des salles de la carte
    e=0
    salles={}
    for i in range(len(grille)):
        for x in range(len(grille[i])):
            if grille[i][x]=="S":
                salles[e]={"x":i,"y":x}
                e=e+1

    return salles


def init_salles(grille,salles):
   salles=salles(grille)
   salles

  L1=range(0,12)
  sallesrempli={"maitrech":{},"savantfou":{}," Bibb1":{},"Bibb2":{},"Bibb3":{},"pinte1":{},"pinte2":{},"pinte3":{},"pinte45":{},"vide":{},"vide":{},"vide":{}}

  for i in range(len(L1)):

      maitrecha=
      savantfou=
      Bibb1=
Bibb2=
Bibb3=
pinte1=
pinte2=
pinte3=
pinte45=
vide=
vide=
vide=



#######MAIN######


grille=initgrille()
affigrille(grille)
a=9
b=5
c="R" # "c"  est la varaiable qui contiendra le précédent contenu de la case où est le personnage
salleco=salles(grille)
while(True):
    affichermenu()
    rep=raw_input()

    if rep=="z":
        grille,a,b,c=deplahaut(grille,a,b,c)
        affigrille(grille)
    elif rep=="q":
        grille,a,b,c=deplagauche(grille,a,b,c)
        affigrille(grille)

    elif rep=="s":
        grille,a,b,c=deplabas(grille,a,b,c)
        affigrille(grille)

    elif rep=="d":
        grille,a,b,c=depladroite(grille,a,b,c)
        affigrille(grille)

    elif rep=="0":
        sys.exit(0)
        affigrille(grille)

#coding: utf8
import sys


def affichermenu():
    print("                    ")

    print("Tapez 1 pour saisir noms et poids ")
    print("Tapez 2 pour afficher le poids max ")
    print("Tapez 3 pour afficher les molécules correspondantes aux cases")
    print("Tapez 4 pour afficher la moyenne des poids ")
    print("Tapez 5 pour afficher les poids supérieur à la moyenne ")
    print("Tapez 6 pour sauvegarder les données dans un fichier ")
    print("Tapez 7 pour recupérer les données depuis un fichier ")
    print("Tapez 0 pour sortir ")


def saisinom(longueur):
    e=0
    longueur=eval(input("Saisir nombre de molécules à saisir"))
    for i in range(longueur):

        x=eval(input("Saisir une molécules"))
        while x in dictnp:
            print("Une molécuels possédent déja un de ces noms,retour menu!")
            print("Recommencez")
            x=eval(input("Saisir une molécules"))

        dictnp[x]=e
        e=e+1


def saisipoids(dictnp):

    for z in list(dictnp.keys()):
        a=int(eval(input("Saisir le poids moléculaires de %s :  "%(z))))
        b=eval(input("Saisir sa chaîne"))
        dictnp[z]={"Poids":a,"Chaine":b}



def poidsmax(dictnp):
    machin=0
    b=0
    if len(dictnp)!=0:
        for e in list(dictnp.keys()):
            if dictnp[e]["Poids"]>b:
                b=dictnp[e]["Poids"]
                machin=e
        print((" Le poids max est de: %.2f pour la molécules de %s"%(b,machin)))
        return b,machin
    else:
            print("Veuillez ajouter d'abord des molécules svp! (Tapez 1)")


def printmole():
    if len(dictnp)!=0:
        for y in list(dictnp.keys()):
            print(("la molécules %s a un poids de %.2f"%(y,dictnp[y]["Poids"])))
    else:
     print("Veuillez ajouter d'abord des molécules svp! (Tapez 1)")


def sumol():
    sum=0.
    if len(dictnp)!=0:
        for x in list(dictnp.keys()):
            sum=sum+ dictnp[x]["Poids"]
        print(("La moyenne des poids est: %.2f"%(sum/len(dictnp))))
        return sum
    else:
         print("Veuillez ajouter d'abord des molécules svp! (Tapez 1)")


def supmoy(sum):
    if len(dictnp)!=0:
        print("Les molécules qui ont un poids supérieur à la moyenne sont:")
        sum=sumol()
        for j in list(dictnp.keys()):
            if dictnp[j]["Poids"]>(sum/len(dictnp)):
                print(("La molécule %s avec un poids de %f"%(j,dictnp[j]["Poids"])))
    else:
         print("Veuillez ajouter d'abord des molécules svp! (Tapez 1)")

def write(dictnp):
     if len(dictnp)!=0:
         nom=eval(input("Indiquez le nom voulu pour le fichier: "))
         fic=open(nom,"w")
         for aze in list(dictnp.keys()):
             fic.write(aze)
             fic.write("\n")
             fic.write(str(dictnp[aze]['Poids']))
             fic.write("\n")
             fic.write(str(dictnp[aze]['Chaine']))
             fic.write("\n")
     else:
         print("Veuillez ajouter d'abord des molécules svp! (Tapez 1)")

def recup():
    nom=eval(input("Indiquez nom du fichier: "))
    ficr=open(nom,"r")
    dictnp={}
    lignes=[]

    for l in ficr.readlines():
        lignes.append(l.strip())
    for i in range(0,len(lignes),3):
         dictnp[lignes[i]]={"Poids":int(lignes[i+1]),"Chaine":lignes[i+2]}

    print(dictnp)
    return dictnp



#main


dictnp={}
longueur=0
truc=0
result=[]
while(True):
       affichermenu()
       rep=eval(input())
       if rep==1:
            saisinom(longueur)
            saisipoids(dictnp)
       elif rep==2:
            poidsmax(dictnp)
       elif rep==3:
            printmole()


       elif rep==4:

          sumol()

       elif rep==5:

           supmoy(sum)

       elif rep==6:
           write(dictnp)

       elif rep==7:
           dictnp=recup()


       elif rep==0:
           sys.exit(0)
       else:
           print(" Erreur de saisie recommençer")

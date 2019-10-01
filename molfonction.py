#coding: utf8


import sys
def affichermenu():
    print "                    "
    
    print "Tapez 1 pour saisir noms et poids "
    print "Tapez 2 pour afficher le poids max "
    print "Tapez 3 pour afficher les molécules correspondantes aux cases"
    print "Tapez 4 pour afficher la moyenne des poids "
    print "Tapez 5 pour afficher les poids supérieur à la moyenne "
    print "Tapez 6 pour sauvegarder les données dans un fichier "
    print "Tapez 0 pour sortir "
    

def saisinom(longueur):
    longueur=input("Saisir nombre de molécules à saisir")
    for i in range(longueur):
        x=raw_input("Saisir une molécules")
        laliste.append(x)

def saisipoids(laliste,laliste2,truc):
    
    for z in range(len(laliste)-truc):
        a=input("Saisir le poids moléculaires de %s :  "%(laliste[truc]))
        laliste2.append(a)
        truc=truc+1
    return truc
def poidsmax(b,machin):
    b=0
    for e in range(len(laliste)):
        if laliste2[e]>b:
            b=laliste2[e]
            machin=e
    print" Le poids max est: %.2f pour la molécules de %s"%(b,laliste[machin])
    return b,machin
def printmole():
    for y in range(len(laliste)):
        print "la molécules dans la case %d est %s avec un poids de %.2f"%(y,laliste[y],laliste2[y])

def sumol():
    sum=0.
    for x in range(len(laliste)):
        sum=sum+ laliste2[x]
    print "La moyenne des poids est: %.2f"%(sum/len(laliste))
    return sum


def supmoy(sum):
    print "Les molécules qui ont un poids supérieur à la moyenne sont:"
    sum=sumol()
    for j in range(len(laliste)):
        if laliste2[j]>(sum/len(laliste)):
            print "La molécule %s avec un poids de %f"%(laliste[j],laliste2[j])
def write(laliste,laliste2):
    fic=open("datamol.txt","w")
    for aze in range(len(laliste)):
        fic.write(laliste[aze])
        fic.write(" ")
        fic.write(str(laliste2[aze]))
        fic.write("\n")
    fic.close()
def read():
    nom=raw_input
    fic2=open(
laliste=[]
laliste2=[]
longueur=0
result=[]
truc=0
while(True):
    affichermenu()
    rep=input()
    if rep==1:
        saisinom(longueur)
        truc=saisipoids(laliste,laliste2,truc)
       
    elif rep==2:
        if len(laliste)!=0:
              poidsmax(laliste,laliste2)
        else:
            print "Veuillez ajouter d'abord des molécules svp! (Tapez 1)"
        
        
    elif rep==3:
        if len(laliste)!=0:
            printmole()
        else:
            print "Veuillez ajouter d'abord des molécules svp! (Tapez 1)"
       
    elif rep==4:
        if len(laliste)!=0:
              sumol()
        else:
            print "Veuillez ajouter d'abord des molécules svp! (Tapez 1)"
      
        
    elif rep==5:
         if len(laliste)!=0:
             supmoy(sum)
         else:
            print "Veuillez ajouter d'abord des molécules svp! (Tapez 1)"
    elif rep==6:
        write(laliste,laliste2)
        
    elif rep==0:
        sys.exit(0)
    else:
        print " Erreur de saisie recommençer"
   
    
       
   




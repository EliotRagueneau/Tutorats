# coding: utf8

import sys
import random 
import os # cette fonction permet de nettoyer l'ecran pour plus de visibilité, mais ne fonctionne que sur Linux
def affichermenu():
    print(' Indiquez votre deplacement avec "1,2,3 ou 5"')
    print(' 5: pour aller vers le haut')
    print(' 1: pour aller vers la gauche')
    print(' 2: pour aller vers le bas')
    print(' 3: pour aller vers la droite')
    print(' --------------------------------')
    print(" Ou 0 pour quitter ")

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


def affigrille(grille):
    for i in grille:
        for x in i:
            print(x, end=' ')
        print(" ")
        
########Déplacements##########
def deplahaut(grille,yjoueur,xjoueur,contenupre):
    if(grille[yjoueur-1][xjoueur]!=" "):
        grille[yjoueur][xjoueur]=contenupre #on attribue le contenu de c à la  case où le personnage va partir 
        contenupre=grille[yjoueur-1][xjoueur] # "contenupre" va prendre le carractère ASCII de la case où le personnage va arrriver 
        yjoueur=yjoueur-1
        xjoueur=xjoueur
        grille[yjoueur][xjoueur]="I"     
    else:
        pass
    return grille,yjoueur,xjoueur,contenupre

def depladroite(grille,yjoueur,xjoueur,contenupre):
    if(grille[yjoueur][xjoueur+1]!=" "):
        grille[yjoueur][xjoueur]=contenupre
        contenupre=grille[yjoueur][xjoueur+1]
        xjoueur=xjoueur+1
        grille[yjoueur][xjoueur]="I"
    else:
        pass
    return grille,yjoueur,xjoueur,contenupre

def deplabas(grille,yjoueur,xjoueur,contenupre):
    if(grille[yjoueur+1][xjoueur]!=" "):
        grille[yjoueur][xjoueur]=contenupre
        contenupre=grille[yjoueur+1][xjoueur]
        yjoueur=yjoueur+1
        grille[yjoueur][xjoueur]="I"
       
    else:
        pass
    return grille,yjoueur,xjoueur,contenupre

def deplagauche(grille,yjoueur,xjoueur,contenupre):
    if(grille[yjoueur][xjoueur-1]!=" "):
        grille[yjoueur][xjoueur]=contenupre
        contenupre=grille[yjoueur][xjoueur-1]
        xjoueur=xjoueur-1
        grille[yjoueur][xjoueur]="I"
        
    else:
        pass
    return grille,yjoueur,xjoueur,contenupre

#########JEU#########
    
def sallesgrille(grille):#pour obtenir les coordonées des salles sur la grille 
    e=0
    salles={}
    for y in range(len(grille)):
        for x in range(len(grille[y])):
            if grille[y][x]=="S":
                salles[e]={"y":y,"x":x}
                e=e+1
    
    return salles
  

def init_salles(grille,salles):
   
   
   
   serierandom=list(range(0,11))
   sallesrempli={"maitrech":1,"savantfou":2,"Bibb1":3,"Bibb2":4,"Bibb3":5,"pinte1":6,"pinte2":7,"pinte3":8,"pinte45":9,"vide":10,"vide":11,"vide":12}
  
   for i in list(sallesrempli.keys()):
	 rchoisi=random.choice(serierandom)
	 sallesrempli[i]={"x":salles[rchoisi]["x"],"y":salles[rchoisi]["y"]}
	 serierandom.remove(rchoisi)
   return sallesrempli

def annonces(grille,yjoueur,b,sallesrempli):
	for cle in list(sallesrempli.keys()):
	
		if (yjoueur,b) in [(sallesrempli[cle]["y"]-1,sallesrempli[cle]["x"]),
					(sallesrempli[cle]["y"]+1,sallesrempli[cle]["x"]),
					(sallesrempli[cle]["y"],sallesrempli[cle]["x"]-1),
					(sallesrempli[cle]["y"],sallesrempli[cle]["x"]+1)]:
			if cle=='maitrech':
				print(" !!!!!! ATTENTION !!!!!! BRUIT DE CLES !!!!!! ")
			if cle=='savantfou':
				print(" !!!!!! HAHAHAHAHAHAHAHAHA !!!!!!")
			if cle=='Bibb1' or cle=='Bibb2'or cle=='Bibb3' : 
				print(" !!!!!! ODEUR DE CHAMALLOW FRAISE !!!!!!!")
			  	
def interaction(grille,yjoueur,xjoueur,contenupre,sallesrempli,venergie):
	for cle2 in list(sallesrempli.keys()):
		
			if yjoueur==(sallesrempli[cle2]["y"]) and xjoueur==(sallesrempli[cle2]["x"]):
				if cle2=='maitrech':
					grille[yjoueur][xjoueur]=contenupre
					contenupre="R"
					yjoueur=9
					xjoueur=5
					print("Vous avez rencontre le maitre du chateau, il vous renvoie à la reception("R") ")
				if cle2=='savantfou':
					grille[yjoueur][xjoueur]=contenupre
					r1=0
					r2=0
					venergie=venergie-1
					while(True):
						r1=random.randrange(len(grille))
						r2=random.randrange(len(grille[r1]))
						if grille[r1][r2]!=" " :
							contenupre=grille[r1][r2]
							yjoueur=r1
							xjoueur=r2
							grille[r1][r2]=1
							print("Vous rencontrez le savant fou il vous envoie dans un endroit aleatoire du chateau")
							break
						
					
				
				if cle2 in ['Bibb1','Bibb2','Bibb3']:
					print("Vous avez rencontre un Bibbindum Chamallow vous perdez 2 pintes d'energie")
					venergie=venergie-2
				
				if cle2 in ['pinte1','pinte2','pinte3', 'pinte45']:
					if cle2=='pinte45':
						venergie=venergie+2
						print("vous trouvez 2 pintes d'energie")
					else:
						venergie=venergie+1
						print("vous trouvez 1 pinte d'energie")
					
					
					sallesrempli[cle2]["x"]=111111#pour supprimer la pinte de la salle
						
						
				resu=0
					
			else:
					resu=1
	return grille,yjoueur,xjoueur,contenupre,sallesrempli,venergie,resu
	
def energie(venergie):

	if venergie<=0:
		print("Votre energie est tombee a 0 vous avez perdu!")
		sys.exit(0)
	else: 
		print("Energie=%i pintes"%(venergie))
def gagnance(grille,yjoueur,xjoueur):
	if yjoueur==1 and xjoueur==11:
		print(" ")
		print(" ")
		print(" ")
		print(" ")
		print("Felicitations vous avez atteint le Paradis, vous remportez la Victoire")
		print(" ")
		print(" ")
		print(" ")
		print(" ")
		sys.exit(0)
   


#######MAIN######    


#definition de certaines variables pour le debut
yjoueur=9#coordonnées en x du joueur(vertical)
xjoueur=5#coordonnées en y du joueur(horizontal)
contenupre="R" #cette variable va contenir le précédent contenu de la case où est le personnage est actuellement, elle est très importante
venergie=3 #le joueur commence avec 3 pintes d'energie

#fonctions d'initialisation:
grille=initgrille()
affigrille(grille)
salles=sallesgrille(grille)
sallesremp=init_salles(grille,salles)

print("Bienvenue au Fantomescape, le but du jeu est de sortir du chateau en atteignant les")
print("portes du paradis, mais attention si votre energie tombe a 0 vous perdez la partie")
print("Vous etes represente par ceci 'I' et vous etes actuellement a la reception 'R'") 
print(" ")
while(True):
    affichermenu()
    rep=input()
    
    if rep=="5":
        grille,yjoueur,xjoueur,contenupre=deplahaut(grille,yjoueur,xjoueur,contenupre)
        
        
    elif rep=="1":
        grille,yjoueur,xjoueur,contenupre=deplagauche(grille,yjoueur,xjoueur,contenupre)
        

    elif rep=="2":
        grille,yjoueur,xjoueur,contenupre=deplabas(grille,yjoueur,xjoueur,contenupre)
       
    elif rep=="3":
        grille,yjoueur,xjoueur,contenupre=depladroite(grille,yjoueur,xjoueur,contenupre)
       
        
    elif rep=="0":
        sys.exit(0)
    os.system('clear')
    print(" ")
    print(" ")
    print(" ")
    annonces(grille,yjoueur,xjoueur,sallesremp)
    grille,yjoueur,xjoueur,contenupre,sallesremp,venergie,resu=interaction(grille,yjoueur,xjoueur,contenupre,sallesremp,venergie)
    while resu!=1:
		grille,yjoueur,xjoueur,contenupre,sallesremp,venergie,resu=interaction(grille,yjoueur,xjoueur,contenupre,sallesremp,venergie)
		
    energie(venergie)
    gagnance(grille,yjoueur,xjoueur)
    affigrille(grille)
   
	

#coding: utf8
#sair 10 molecules, les stocker dans une liste, afficher la lsite "la molécules dans la case 0 est NADH"
laliste=[]
laliste2=[]
sum=0.
b=0
longueur=0
result=[]
longueur=eval(input("Saisir nombre de molécules à saisir"))
for i in range(longueur):
    x=eval(input("Saisir une molécules"))
    laliste.append(x)


for z in range(longueur):
    a=eval(input("Saisir un poids moléculaires"))
    laliste2.append(a)
    if a>b:
        b=a
        machin=z
for y in range(longueur):
    print(("la molécules dans la case %d est %s avec un poids de %.2f"%(y,laliste[y],laliste2[y])))
print((" Le poids max est: %.2f pour la molécules de %s"%(b,laliste[machin])))
for x in range(longueur):
    sum += laliste2[x]

print(("La moyenne des poids est: %.2f"%(sum/longueur)))
print("Les molécules qui ont un poids supérieur à la moyenne sont: ") 
for j in range(longueur):
    if laliste2[j]>(sum/longueur):
       print(("La molécule %s avec un poids de %f"%(laliste[j],laliste2[j])))





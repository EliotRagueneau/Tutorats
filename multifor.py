#coding: utf8
a=eval(input("Choisir un premier entier: "))
b=eval(input("Choisir un deuxième entier: "))
if(a>b):
    a,b=b,a
for a in range (a,b+1):
    i=1
    for i  in range (11):
         print(("%d x %d =%d"%(a,i,a*i)))
         i=i+1
    a=a+1
    print(" ")

    

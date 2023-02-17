import matplotlib.pyplot as plt
from random import *
import time
from math import *

###########################################

def TableauAuHasard(n):
    TabHasard=[]
    for i in range(0,n):
        TabHasard.append(randint(1,1000)) 
    return TabHasard

def ChoixPivot(n,T,typepivot):
    p = 0
    if(typepivot == 2): #Pivot cours
        nInf = n
        nSup = n
        while(nInf > ceil(3*n//4) or nSup > ceil(3*n//4)):
            p = randint(0,n-1)
            nInf = 0
            nSup = 0
            for i in range(0,n):
                if(T[i] > T[p]):
                    nSup += 1
                if(T[i] < T[p]):
                    nInf += 1
    if(typepivot == 3): #Pivot aléatoire
        p = randint(0,n-1)
    return p


def Rang(n,k,T,typepivot):
    if(k==1):
        return T[0]
    if(T == []):
        return -1
    if n==1:
         return T[0]
    p = ChoixPivot(n, T, typepivot)
    nInf=0
    nSup=0
    nEq=0
    Tinf=[]
    Tsup=[]
    for i in range(0,n):
        if (T[i] < T[p]):
            Tinf.append(T[i])
            nInf += 1
        elif (T[i] > T[p]):
            Tsup.append(T[i])
            nSup += 1
        else:
            nEq += 1
    if(k < nInf): #k est dans le min
        print(T[p]," Inf: ",Tinf)
        print("k: ",k)
        return Rang(nInf,k,Tinf,typepivot)
    elif(k < nInf+nEq): #k est dans le eq
        return T[p]
    else: #k est dans le sup
        print(T[p]," Sup: ",Tsup)
        print("k: ",k-(nInf+nEq))
        return Rang(nSup,k-nInf-nEq,Tsup,typepivot)

#######Programme Principal########

choix=int(input("Taper 1 pour l'exemple pré-rentré, 2 pour un tableau aléatoire: "))
if choix==1:
    n=12
    Tab=[34,12,4,5,67,7,42,13,45,9,2,31]
else:
    n=int(input("Rentrer la taille du tableau aléatoire: "))
    Tab=TableauAuHasard(n)    

typepivot=int(input("Taper 1 pour un pivot fixe (T[0]), taper 2 pour le choix de pivot du cours et taper 3 pour un pivot aléatoire: "))
npivot=0
nappelChoixPivot=0

rang=int(input("Entrer le rang à déterminer: "))
print("Tableau d'entrée: ",Tab)
print("Rang trouvé: ", Rang(n,rang,Tab,typepivot))

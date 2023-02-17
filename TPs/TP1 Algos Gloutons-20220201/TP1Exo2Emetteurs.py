from random import *
from math import sqrt
from itertools import *
import matplotlib.pyplot as plt

def AfficheMaisons(Maison):
    n=len(Maison)
    BonEmetteur = []
    for i in range(0,len(Maison)):
        if Emetteur[i]==1:
            BonEmetteur.append(Maison[i])
    plt.plot([m[0] for m in Maison],[m[1] for m in Maison],'bo',markersize =3,label='maison')
    plt.plot([m[0] for m in BonEmetteur],[m[1] for m in BonEmetteur],'bo',markersize =3,label='maisonEmetteurs',color='g')
    plt.title(str(n)+' Maisons')
    plt.legend()
    plt.axis('equal')
    plt.show()

def AfficheEmetteurs(Maison,Emetteur,rayon):
    n=len(Maison)
    fig, ax = plt.subplots()
    for i in range(n):
        if Emetteur[i]==1:
            circle=plt.Circle(Maison[i],rayon, color='r')
            ax.add_artist(circle)
    AfficheMaisons(Maison)


def GenererMaisons(Maison,n):
    for i in range(0,n):
        Maison.append([randint(1,1100),randint(1,1100)])

def Couvre(Maison,i,j):
    distanceX = max(Maison[i][0],Maison[j][0])-min(Maison[i][0],Maison[j][0])
    distanceY = max(Maison[i][1],Maison[j][1])-min(Maison[i][1],Maison[j][1])
    distance = sqrt(distanceX**2 + distanceY**2)
    if(distance <= rayon): 
        return True
    else: 
        return False


def choixMaison(Maison,MaisonsRestantes):#MaisonsRestantes[i]=0 ssi i n'est pas couverte
    i0=-1
    nbCouvreMax = 0
    nbCouvreMaxLocal = 0
    for i in range(0,len(Maison)):
        for j in range(0,len(Maison)):
            if Couvre(Maison,i,j) and (MaisonsRestantes[j]==0):
                nbCouvreMaxLocal+=1
        if(nbCouvreMaxLocal > nbCouvreMax):
            nbCouvreMax = nbCouvreMaxLocal
            i0=i
    return i0

#Approx gloutonne
def choixEmetteurGlouton(Maison):
    n=len(Maison)
    Emetteur=[0]*n
    MaisonsRestantes=[0]*n
    while(MaisonsRestantes != [1]*n):
        MeilleurIndice = choixMaison(Maison,MaisonsRestantes)
        Emetteur[MeilleurIndice] = 1
        MaisonsRestantes[MeilleurIndice] = 1
        for j in range(0,n):
            if Couvre(Maison,MeilleurIndice,j) and (MaisonsRestantes[j]==0):
                MaisonsRestantes[j] = 1
    return Emetteur
    
    
rayon=120 # rayon de l'émetteur
n=100 #nombre de maisons
Maison=[] #contient les coordonnees cartesiennes des maisons dans [1,1000]x[1,1000]
Emetteur=[0]*n
GenererMaisons(Maison,n)
AfficheMaisons(Maison)
Emetteur=choixEmetteurGlouton(Maison)
nbEmetteur = 0
for i in range(0,len(Emetteur)):
    if Emetteur[i]==1:
        nbEmetteur+=1
print("L'algo glouton place",nbEmetteur,"émetteurs")
AfficheEmetteurs(Maison,Emetteur,rayon)

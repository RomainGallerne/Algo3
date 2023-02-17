from random import *
import operator

def CoursAuHasard(n):
    Cours=[]
    for i in range(0,n):
        début = randint(1,90)
        durée = randint(0,10)
        Cours.append([début,début+durée])
    return Cours

def TriBulles(Cours):
    for j in range(0,n):
        for i in range(0,n-1):
            if Cours[i][1] > Cours[i+1][1]:
                Cours[i],Cours[i+1] = Cours[i+1],Cours[i]
    print("Cours triés par dates de fin croissantes: \n",Cours)

def glouton(Cours):
    TriBulles(Cours)
    L = [Cours[0]]
    fin = Cours[0][1]
    for i in range(1,n):
        if Cours[i][0] >= fin:
            L.append(Cours[i])
            fin = Cours[i][1]
    return L

   
#=================================================================

alea=int(input('Taper 1 pour utiliser l\'exemple pré-rempli, taper 2 pour choisir une instance au hasard:'))
if alea==1:
    n=30
    Cours=[[70, 75], [15, 16], [64, 66], [3, 4], [40, 46], [51, 52], [4, 14], [59, 61], [47, 49], [33, 35], [12, 17], [41, 49], [59, 60], [30, 35], [31, 33], [57, 64], [40, 50], [30, 40], [68, 73], [24, 25], [40, 46], [63, 73], [75, 82], [20, 26], [58, 67], [60, 67], [69, 70], [31, 39], [43, 50], [10, 20]]  
else:
    n=int(input('Entrez le nombre de cours: '))
    Cours=CoursAuHasard(n)
print("Ensemble de cours disponibles: \n",Cours)
print("Choix de cours effectué :", glouton(Cours))

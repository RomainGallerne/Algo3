import matplotlib.pyplot as plt
from random import *
import time

###########################################

def TableauAuHasard(n):
    TabHasard=[0]*n
    for i in range(0,n):
        TabHasard[i]=randint(1,10000)
    return TabHasard

def TriFusion(n,T):
    global nbAppelRec 
    nbAppelRec += 1
    if n>1:
        n1=n//2 
        n2=n-n1 
        T1=[0]*n1
        T2=[0]*n2
        for i in range(0,n1):
            T1[i] = T[i]
        for j in range(n1,n):
            T2[j-n1] = T[j]
        Fusion(n1,n2,TriFusion(n1,T1),TriFusion(n2,T2),T)
    return T


def Fusion(n1, n2, T1, T2, T):
    i1 = 0
    i2 = 0
    for i in range(0,n1+n2):
        if(i1<n1):
            if(i2 >= n2 or T1[i1] <= T2[i2]):
                    T[i] = T1[i1]
                    i1+=1
            else:
                T[i] = T2[i2]
                i2+=1
        else:
            T[i] = T2[i2]
            i2+=1 
    return T

def TriBulles(n,T):
    for i in range(0,n):
        for j in range(i,n):
            if T[j] < T[i]:
                T[i],T[j] = T[j],T[i]

#######Programme Principal########

nbAppelRec = 0
choix=int(input("Taper 1 pour un test sur le TriFusion, 2 pour un comparatif TriFusion/TriBulles: "))
if choix==1:
    Tab=[0]
    n=int(input("Entrez la taille du tableau à trier: "))
    Tab=TableauAuHasard(n)
    print("Tableau à trier: ",Tab)
    TabFusion=list(Tab)
    TriFusion(n, TabFusion)
    print("Après TriFusion: ",TabFusion)
    TabBulles=list(Tab)
    TriBulles(n, TabBulles)
    print("Après TriBulles: ",TabBulles)
else:    
    #Valeurs de n choisies    
    abscisses = [n for n in range(1,1000,10)]
    #Temps de calcul
    tps1 = []
    tps2 = []
    for n in range(1,1000,10):
        T=TableauAuHasard(n)
        T2=list(T)
        t=time.time()
        TriBulles(n, T)
        tps1.append(time.time()-t)
        t=time.time()
        TriFusion(n, T2)
        tps2.append(time.time()-t)
    #Tracé
    plt.plot(abscisses, tps1)
    plt.plot(abscisses, tps2)
    plt.show()
print("NbAppelRec : ",nbAppelRec)
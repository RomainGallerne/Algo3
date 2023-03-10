import matplotlib.pyplot as plt

#######Classe Noeud#######
class Noeud:
   def __init__(self, val=None):
      self.val = val
      self.FilsG = None
      self.FilsD = None
      self.Pere = None

   def HauteurNoeud(self):
       hg=0
       hd=0
       if self.FilsG!=None:
           hg=self.FilsG.HauteurNoeud()
       if self.FilsD!=None:
           hd=self.FilsD.HauteurNoeud()
       return max(hd,hg)+1

 
#######Classe Arbre Binaire#######
class ArbreBinaire:
   def __init__(self):
        self.rac=None

   def AjoutRacine(self,val):
       nouvNoeud=Noeud(val)
       self.rac=nouvNoeud

   def AjoutNoeudFilsG(self,x,val):
       if x.FilsG==None:
           nouvNoeud=Noeud(val)
           x.FilsG=nouvNoeud
           nouvNoeud.Pere=x

   def AjoutNoeudFilsD(self,x,val):
       if x.FilsD==None:
           nouvNoeud=Noeud(val)
           x.FilsD=nouvNoeud
           nouvNoeud.Pere=x

   def DessinArbreNiveau(self,nx,rect,dy):
       if nx==None: return
       x1, x2, y1, y2 = rect
       xm = (x1 + x2) // 2
       self.DessinArbreNiveau(nx.FilsG, (x1, xm, y1, y2 - dy), dy)
       self.DessinArbreNiveau(nx.FilsD, (xm, x2, y1, y2 - dy), dy)
       plt.text(xm + 10, y2, str(nx.val), fontsize=10, horizontalalignment='left',verticalalignment='bottom')
       if nx.FilsG!=None:
          a, b = ((xm, (x1 + xm) // 2), (y2, y2 - dy))
          plt.plot(a, b, 'k', marker='s')
       if nx.FilsD!=None:
          c, d = ((xm, (x2 + xm) // 2), (y2, y2 - dy))
          plt.plot(c, d, 'k', marker='s')

   def DessinArbre(self):
        d = 512
        pad = 20
        dy = (d - 2 * pad) / self.rac.HauteurNoeud()
        self.DessinArbreNiveau(self.rac, (pad, d - pad, pad, d - pad), dy)
        plt.axis([0, d, 0, d])
        plt.axis('off')
        plt.show()
        
################################################        
        
def Maximum(x):
    if (x.FilsG != None):
        if (x.FilsD != None):
            maxFils = max(Maximum(x.FilsG),Maximum(x.FilsD))
        else:
            maxFils = Maximum(x.FilsG)
    elif (x.FilsD != None):
        maxFils = Maximum(x.FilsD)
    else:
        maxFils = x.val
    return max(x.val,maxFils)

def ParcoursInfixe(x):
    if (x!=None):
        return str(ParcoursInfixe(x.FilsG)) + str(x.val) + str(ParcoursInfixe(x.FilsD))
    else: return " "

def ParcoursPrefixe(x):
    if (x!=None):
        return str(x.val) + str(ParcoursInfixe(x.FilsG)) + str(ParcoursInfixe(x.FilsD))
    else: return " "

def ParcoursSufixe(x):
    if (x!=None):
        return str(ParcoursInfixe(x.FilsG)) + str(ParcoursInfixe(x.FilsD)) + str(x.val)
    else: return " "

def Inserer(ABR,z):
    x=ABR.rac    
    p=None
    while(x!=None):
        p=x
        if (z.val < x.val):
            x = x.FilsG
        else: x = x.FilsD
    z.Pere = p
    if (p==None): ABR.rac = z
    else: 
        if (z.val < p.val):
            p.FilsG = z
        else: p.FilsD = z

def CreerABR(ArbRech,L):
    for i in range(0,len(L)):
        Inserer(ArbRech,Noeud(L[i]))

def RechercheCle(ABR,k):
    x=ABR.rac
    while(x != None):
        if (x.val == k):
            return True
        elif (x.val > k):
            x = x.FilsG
        else:
            x = x.FilsD
    return False

#######Arbre Binaire########
Arb=ArbreBinaire()
Arb.AjoutRacine(3)
Arb.AjoutNoeudFilsG(Arb.rac, 5)
Arb.AjoutNoeudFilsD(Arb.rac, 7)
Arb.AjoutNoeudFilsD(Arb.rac.FilsG, 1)
Arb.AjoutNoeudFilsG(Arb.rac.FilsG, 14)
Arb.AjoutNoeudFilsD(Arb.rac.FilsD, 8)
Arb.AjoutNoeudFilsG(Arb.rac.FilsD.FilsD, 15)
Arb.AjoutNoeudFilsG(Arb.rac.FilsG.FilsD, 24)
Arb.AjoutNoeudFilsD(Arb.rac.FilsG.FilsD, 2)
print("Arbre Binaire : Maximum des valeurs de l'arbre: ",Maximum(Arb.rac))
print("Arbre Binaire : Parcours Infixe: [",ParcoursInfixe(Arb.rac),"]")
print("Arbre Binaire : Parcours Prefixe: [",ParcoursPrefixe(Arb.rac),"]")
print("Arbre Binaire : Parcours Sufixe: [",ParcoursSufixe(Arb.rac),"]")
print("Arbre Binaire : Insertion du noeud 11")
Inserer(Arb, Noeud(11))
print("\n")
Arb.DessinArbre()

#######Arbre Binaire de Recherche########
L=[16,6,3,19,8,7,17,20,23,1,5,13,22,14,12]
ArbRech = ArbreBinaire()
CreerABR(ArbRech, L)
print("Arbre Recherche : Existe-il un noeud 15 ? ",RechercheCle(ArbRech, 15))
ArbRech.DessinArbre()
#CreerABR(ABR,L)
#ABR.DessinArbre()
#RechercheCle(ABR,23)


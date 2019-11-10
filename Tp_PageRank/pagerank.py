import numpy as np
from scipy.spatial import distance

f=open("tiny-graph.txt","r")
fact_amort=0.1
epsilon=10**(-5)
f1=f.readlines()
N=int (f1[0])
del(f1[0])
A= np.zeros((N,N))
for x in f1:
    list=x.split(" ")
    ind_ligne=int(list[0])
    del(list[0])
    for j in list:
        indice_colonne=int(j)
        A[ind_ligne,indice_colonne]=1

#génération aléatoire de la matrice A :
#
#tirage nb alea -> Nombre_page
#ecriture dans fichier de Nombre Page
#for i in range(Nombre Page):
#   list_lien_curr_page=[]
#   tirage alea entre 0 et Nombre page -> nb_lien_sortant pour la page d'indice i
#    for j in range(nb_lien_sortant):
#       tirage aleatoire entre 0 et Nombre Page -> ind_alea_lien
#       while nb_alea_lien in list_lien_curr_page:
#            tirage aleatoire entre 0 et Nombre Page -> ind_alea_lien
#       list_lien_curr_page.append(ind_alea_lien)
#   for j in list_lien_curr_page:
#       ecrire fichier (j+" ")
#   print("\n")
#fermer fichier 

            


P=np.zeros((N,N), dtype=float)
for i in range (N):
    somme=0
    for j in range (N):
        somme=somme+A[i,j]
    for j in range(N):
        if somme!=0 :
            P[i,j]=fact_amort*(A[i,j]/somme)+(1-fact_amort)*(1/N)
        else :
            P[i,j]=1/N



R=np.zeros(N)
for i in range (N):
    R[i]=1/N

R_suivant=np.zeros(N)

l=0

def dist(x,y):
    return np.sqrt(np.sum((x-y)**2))

R_suivant=np.dot(R,P)
print(R_suivant)

while (dist(R_suivant,R) >= epsilon) :
    l=l+1
    print(l)
    print(R)
    print(R_suivant)
    print(dist(R_suivant,R))

    R = R_suivant
    R_suivant = np.dot(R,P)
     #print(R_suivant)


print(R)

#1. On observe que le nombre d'itérations augmente sensiblement quand epsilon diminue, cependant le ranking de chaque page reste relativement similaire d'une itération à l'autre, d'ou l'importance de choisir un critere d'arret cohérent en fonction de la précision que nous désirons

#2. Ce sont les pages qui on beaucoup de liens entrant qui en général on le meilleur ranking 

#3. pour améliorer le rang d'une page on peut par exemple rediriger la sortie des pages les mieux classé vers la page dont l'on veut améliorer le rang, faire en sorte qu'elle soit la page "centrale" des autres pages

#4. quand lambda tend vers 0 la tendance décrite précédemment n'est plus valide, en effet le rang des pages semble se stabiliser et atteindre une moyenne pour toutes les pages 

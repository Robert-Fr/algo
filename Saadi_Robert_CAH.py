import numpy as np
#la matrice de similarité
sim_mat = np.array ([[10,6,0,0,0,0,0,0,0],[6,10,0,0,0,0,0,0,0],[0,0,10,5,3,3,1,1,0],[0,0,5,10,1,2,1,1,0],[0,0,3,1,10,4,1,2,0],[0,0,3,2,4,10,1,4,0],[0,0,1,1,1,1,10,1,0],[0,0,1,1,2,4,1,10,0],[0,0,0,0,0,0,0,0,10]])
#matrice qui dit si une classe est active ou non 
I = np.ones((9,), dtype=int)
#matrice qui contient les files a priorités pour les N documents
p=sim_mat

N=9
#Fonction permettant d'enlever la diagonale de la matrice de similarité
def remove_diag(x):
    x_no_diag = np.ndarray.flatten(x)
    x_no_diag = np.delete(x_no_diag, range(0, len(x_no_diag), len(x) + 1), 0)
    x_no_diag = x_no_diag.reshape(len(x), len(x) - 1)
    return x_no_diag

p=remove_diag(p)
#On tri les listes de priorités
for i in range(0,8) :
    p[i,]=sorted(p[i,],reverse=True)
#On initialise la liste des fusions
l=[]

#Les N-1 itérations correspondantes au nombre de fusions possible sur N éléments
for k in range(N-1) :
    # for a in range(N):
        # if I[a]==1 :
            # print(p[a,])
        # else :
                        # print(" inactif")
    max=-1
    indic_max=-1
    i1=-1
    #on cherche i1
    for i in range(N) :
        if p[i,0]>max and I[i]==1:
            max=p[i,0]
            indic_max=i
    i1=indic_max
    
    #on cherche i2 : C'est l'indice qui correspond à la similarité max (trouvé au dessus), dans la matrice de similarité
    for j in range(N):
        if ((sim_mat[indic_max,j]==max) and (I[j]!=0)):
            i2=j
            print(I[j])
            break
    
    #on ajoute la fusion entre i1 et i2
    l.append((i1,i2))
    #on considère que i1 est la classe qui reste active
    I[i2]=0
    
    p[i1,0]=-1
    # print ("i1 = " + str(i1) + " a l'etape " + str(k) )
    # print ("i2 = " + str(i2) + " a l'etape " + str(k) )
    # print ("max = " + str(max) + " a l'etape " + str(k) )
    
    #Pour tout les documents qu'il reste a fusionner :
    for i in range(N) :
        if I[i]==1 and i!=i1 :
            #on supprime sim_mat[i,i2] de p[i]
            for j in range(N - 1):
                if p[i, j] == sim_mat[i, i2]:
                    p[i, j] = -1
                    break
                    
            #si max(S[i][i1],S[i][i2]) = S[i][i1]
            if sim_mat[i,i1]>sim_mat[i,i2] :
                sim_mat[i,i1]=sim_mat[i,i1]
                sim_mat[i1, i] = sim_mat[i, i1]
                for j in range(N - 1):
                    if p[i, j] == sim_mat[i, i1]:
                        p[i, j] = sim_mat[i, i1]
                        break
                for j in range(N - 1):
                    if p[i1, j] == sim_mat[i1, i]:
                        p[i1, j] = sim_mat[i, i1]
                        break
            #si max(S[i][i1],S[i][i2]) = S[i][i2]
            else :
                sim_mat[i, i1] = sim_mat[i, i2]
                sim_mat[i1, i] = sim_mat[i, i2]
                for j in range(N - 1):
                    if p[i, j] == sim_mat[i, i1]:
                        p[i, j] = sim_mat[i, i2]
                        break
                for j in range(N - 1):
                    if p[i1, j] == sim_mat[i1, i]:
                        p[i1, j] = sim_mat[i, i2]
                        break
        #on retrie nos listes de priorités
        for m in range(N):
            p[m,] = sorted(p[m,], reverse=True)
    

print (l)




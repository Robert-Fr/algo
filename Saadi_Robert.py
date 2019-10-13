#la dimension de la matrice de similarité = nombre de document, dans notre exemple 10
N=10
#pour accéder a sim_mat[i][j] il faut faire : (i * N) + j
sim_mat = [10,6,0,0,0,0,0,0,0,6,10,0,0,0,0,0,0,0,0,0,10,5,3,3,1,1,0,0,0,5,10,1,2,1,1,0,0,0,3,1,10,4,1,2,0,0,0,3,2,4,10,1,4,0,0,0,1,1,1,1,10,1,0,0,0,1,1,2,4,1,10,0,0,0,0,0,0,0,0,0,10]

#on initialise la matrice P : liste de tuple : le premier élément est la similarité la plus haute associé au docuent d'indice i, e deuxième élément est l'index du document avec qui il y a la plus forte similarité
def init_P (N,sim_mat) :
    P=[]
    for i in range(N):
        # recherche de la plus grosse sim pour mettre le tuple (sim,index) dans P[i]
        sim_max=0
        ind_sim_max=0
        for k in range(N):
            if k != i :
                if sim_max < sim_mat[k*N+i]:
                    ind_sim_max=k
                    sim_max=sim_mat[k*N+i]
        P.append( (sim_max,ind_sim_max) )
    return P    
    
# on initialise la matrice I :
def init_I (N) :
    I=[]
    for i in range(N):
        I.append(i)
    return I
    


def partitionement_hierarchique_aglommeratif ( N,sim_mat) :
    #on initialise nos structures de données :
    I=init_I(N)
    P=init_P(N,sim_mat)
    L = []
    
    #pour toute les itérations :
    for k in range(N-1):
    
        #on prend la liste des classes active
        for i in range(N):
            if I[i]==i :
                list_classe_active.append(i)
        #on prend la classe active qui a la plus grosse similarité possible avec une autre classe
        sim_max=0
        ind_sim_max=0
        for i in list_classe_active:
            (sim,ind)=P[i]
            if  sim>sim_max:
                sim_max=sim
                ind_sim_max=ind
        #on a i1
        i1=ind_sim_max
        #i2 est la classe à laquelle appartient le document qui est le plus proche de i1
        (sim,ind) = P[i1]
        i2=I[ind]
        #on met P[i1].sim = -1
        P[i1]=(-1,ind)
        #on Fusionne i1 et i2 :
        L.append( (i1,i2) )
        
        for i in range(N):
            #on met à jour les similarités pour les éléments qui n'ont pas été fusionnés dans cette itération :
            if (I[i] == i) and (i != i1) and (i != i2) :
                #S[i][i1]= max( S[i][i1] , S[i][i2] )
                #S[i1][i]= max( S[i][i1] , S[i][i2] )
                if sim_mat[i*N + i1] > sim_mat[i*N + i1] :
                    sim_mat[i*N + i1]=sim_mat[i*N + i1] 
                    sim_mat[i1*N + i]=sim_mat[i*N + i1]
                else :
                    sim_mat[i*N + i1]=sim_mat[i*N + i2] 
                    sim_mat[i1*N + i]=sim_mat[i*N + i2]
            #On met à jour la classe active pour la classe fusionné lors de cette itération:
            if I[i]==i2 :
                I[i]=i1
            
            #on met à jour la matrice P pour la prochaine itération :
            (sim,ind)=P[i1]
            if (I[i] == i) and (i != i1) and ( sim_mat[ (i1 * N) + i ] > sim ) :
                P[i1]=(sim_mat[ (i1 * N) + i ] , i)
    #on retourne la liste des fusions obtenue
    return L
        
    
Liste_fusion =partitionement_hierarchique_aglommeratif(N,sim_mat)
print(L)
    
    
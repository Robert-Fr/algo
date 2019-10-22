import numpy as np
sim_mat = np.array ([[10,6,0,0,0,0,0,0,0],[6,10,0,0,0,0,0,0,0],[0,0,10,5,3,3,1,1,0],[0,0,5,10,1,2,1,1,0],[0,0,3,1,10,4,1,2,0],[0,0,3,2,4,10,1,4,0],[0,0,1,1,1,1,10,1,0],[0,0,1,1,2,4,1,10,0],[0,0,0,0,0,0,0,0,10]])
I = np.ones((9,), dtype=int)

p=sim_mat

N=9

def remove_diag(x):
    x_no_diag = np.ndarray.flatten(x)
    x_no_diag = np.delete(x_no_diag, range(0, len(x_no_diag), len(x) + 1), 0)
    x_no_diag = x_no_diag.reshape(len(x), len(x) - 1)
    return x_no_diag

p=remove_diag(p)
for i in range(0,8) :
    p[i,]=sorted(p[i,],reverse=True)

l=[]

for k in range(N-1) :
    max=-1
    indic_max=-1
    i1=-1
    #on cherche i1
    for i in range(N) :
        if p[i,0]>max and I[i]==1:
            max=p[i,0]
            indic_max=i
    for j in range(N-1):
        if sim_mat[indic_max,j]==max :
            i1=j
            break
    #on cherche i2
    for j in range(N - 1):
        if sim_mat[i1, j] == p[i1,0]:
            i2 = j
            break
    #on ajoute la fusion entre i1 et i2
    l.append((i1,i2))
    I[i2]=0
    p[i1,0]=-1
    print ("i1 = " + str(i1) + " a l'etape " + str(k) )
    print ("i2 = " + str(i2) + " a l'etape " + str(k) )
    print ("max = " + str(max) + " a l'etape " + str(k) )

    for i in range(N) :
        if I[i]==1 and i!=i1 :
            #on supprime sim_mat[i,i2] de p[i]
            for j in range(N - 1):
                if p[i, j] == sim_mat[i, i2]:
                    p[i, j] = -1
                    break
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
        for m in range(N):
            p[m,] = sorted(p[m,], reverse=True)
    for a in range(N):
        if I[a]==1 :
            print(p[a,])
        else :
                        print(" inactif")

print (l)




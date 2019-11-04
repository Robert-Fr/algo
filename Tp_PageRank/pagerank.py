import numpy as np

f=open("tiny-graph.txt","r")
fact_amort=0.85
epsilon=10^(-3)
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

for i in range (N) :
    print(A [i])


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

for i in range (N) :
    print(P[i])

R=np.zeros(N)
for i in range (N):
    R[i]=1/N

R_suivant=np.zeros(N)

l=0

while(True) :
    if l==0 :
        R_suivant=np.dot(R,P)
        l=l+1
    else :
        if (R_suivant-R) <= epsilon :
            break
        else :
            R_suivant = np.dot(R,P)
            l = l + 1

print(R)

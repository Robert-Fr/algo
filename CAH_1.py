import numpy as np
sim_mat = np.array ([[10,6,0,0,0,0,0,0,0],[6,10,0,0,0,0,0,0,0],[0,0,10,5,3,3,1,1,0],[0,0,5,10,1,2,1,1,0],[0,0,3,1,10,4,1,2,0],[0,0,3,2,4,10,1,4,0],[0,0,1,1,1,1,10,1,0],[0,0,1,1,2,4,1,10,0],[0,0,0,0,0,0,0,0,10]])
indic_classes = np.ones((9,), dtype=int)
print(indic_classes)
p=sim_mat

def remove_diag(x):
    x_no_diag = np.ndarray.flatten(x)
    x_no_diag = np.delete(x_no_diag, range(0, len(x_no_diag), len(x) + 1), 0)
    x_no_diag = x_no_diag.reshape(len(x), len(x) - 1)
    return x_no_diag

p=remove_diag(p)
for i in range(0,8) :
    p[i,]=sorted(p[i,],reverse=True)

print(p)

l=[]




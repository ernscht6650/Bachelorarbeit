from qutip import *
import numpy as np


def ID (n):
    I=identity(2)
    for k in range(1,n):
        I=tensor(I,identity(2))
      #  print(k,n, "\n", I)
    return I

def Int (n):
    A=tensor(sigmaz()-identity(2),ID(N-1))
    for  k in range(2, n+1):
        A+=tensor(ID(k-1), sigmaz()+(-1)**k*identity(2), ID(N-k))
    A=A*A/4
    return A;

m=0
g=1

L=1
N=10
for y in range(1, 10, 1):

    SIG=tensor(sigmap(),sigmam())+tensor(sigmam(),sigmap())

    V=tensor(SIG,ID(N-2))

    for n in range(2,N-1):
        V+=tensor(ID(n-1),SIG,ID(N-n-1))

    V+=tensor(ID(N-2),SIG)

    #print(V)

    E=Int(1)
    for n in range(2,N):
        E+=Int(n)

    #print(E)

 
    W=E+100*V/(y**2)

    U=V.eigenenergies()

    print(U[0]/N, "\n")
    Mg=y*(U[1]-U[0])/20

    #print(1/N**2, Mdurchg)
    print(y/10, Mg)



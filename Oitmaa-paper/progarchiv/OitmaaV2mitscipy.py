import numpy as np
from scipy.sparse import *

dense_matrix = np.array([[0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]])

h = csr_matrix(dense_matrix)



sigmax=csr_matrix(np.array([[0,1],[1, 0]]))
sigmaz=csr_matrix(np.array([[1,0],[0,-1]]))
sigmap=csr_matrix(np.array([[0,1],[0,0]]))
sigmam=csr_matrix(np.array([[0,0],[1,0]]))

#Terme des Hamiltonians
def Herm (A):
    return np.conjugate(np.transpose(A))

def Inter (n,M):
    A=kron(sigmaz-eye_array(2),eye_array(2**(M-1)))
   # print(0, "\n", A)
    for  k in range(2, n+1):
        xi=kron(eye_array(2**(k-1)), sigmaz+(-1)**k*eye_array(2))
        #print(1, k,"\n",xi)#, eye_array(2**(M-k))))
        A+=kron(xi, eye_array(2**(M-k)))
        #print(A)
        #A+=kron(eye_array(2**(k-1)), sigmaz+(-1)**k*eye_array(2), eye_array(2**(M-k)))
    A=A@A/4
    return A;

def WL (M):
    A=Inter(1,M)
    for n in range(2,M):
        A+=Inter(n,M)
    return A

def V (M):
    if M<4:
        return h
    else:
        A=kron(h,eye_array(2**(M-2)))
    
        for n in range(2,M-1):
            xi=kron(eye_array(2**(n-1)),h)
            A+=kron(xi,eye_array(2**(M-n-1)))

        A+=kron(eye_array(2**(M-2)),h)

        return A

def MassTerm (M):
    A=-1*kron(sigmaz, eye_array(2**(M-1)))+M*eye_array(2**M)
    for k in range(2,M):
        xi=kron(sigmaz, eye_array(2**(M-k)))
        A+=(-1)**k*kron(eye_array(2**(k-1)), xi)
    A+=(-1)**M*kron(eye_array(2**(M-1)), sigmaz)
    return 0.5*A

def S (M):
    A=kron(sigmaz, eye_array(2**(M-1)))
    for k in range(2,M):
        xi=kron(sigmaz, eye_array(2**(M-k)))
        A+=kron(eye_array(2**(k-1)), xi)

    A+=kron(eye_array(2**(M-1)), sigmaz)
    return A

def findZeros (M): #Bestimme zustände mit Gesamtspin 0
    A=np.where(S(M).diagonal() == 0)[0]
    return A

# entferne zustände mit gesamtspin ungleich Null

def NonZeroSpin_entferner (H,M):
    indices=findZeros(M)
    Vprime=csr_matrix(H)[indices,:]
    Vprimeprime=Vprime[:, indices]

    return Vprimeprime

def Op (N,x):
    Xi=kron(sigmam,kron(sigmaz,sigmap))-kron(sigmap,kron(sigmaz,sigmam))
    if N<4:
        return -x*Xi
    else:
        A=kron(Xi, eye_array(2**(N-3)))
        for k in range(2,N-2):
            A+=kron(eye_array(2**(k-1)),kron(Xi,eye_array(2**(N-2-k))))

        A+=kron(eye_array(2**(N-3)), Xi)
        return -x*A #sieht aus als würde das j nix machen

def Translation(N): #verschiebt Spins um einen Gitterplatz
    A=lil_array(0*eye_array(2**N))
    for n in range(0,2**(N-1)):
        A[n,2*n]=1
    for k in range(2**(N-1),2**N):
        A[k,2*k-2**N+1]=1
    return csr_matrix(A)

def Antidiag(N): #verschiebt Spins um einen Gitterplatz
    A=lil_array(0*eye_array(2**N))
    for n in range(0,2**N):
        A[n,2**N-1-n]=1
    return csr_matrix(A)


def SR (N):
   # A=sigmax
    #for i in range(2,N+1):
    #    A=kron(A,sigmax)
    return Antidiag(N)@Translation(N)

def SR2 (N):
    A=kron(sigmax,eye_array(2))
    for i in range(1,int(N/2)):
        A=kron(A,sigmax)
        A=kron(A, eye_array(2))

    return A@Translation(N)


def M1durchg (mdurchg):
    for Volume in range(5,26,5):
        for N in range(4, 26, 2):
            y=Volume/N
            mu=2*mdurchg/y
            Wprime=NonZeroSpin_entferner(V(N)/(y**2)+WL(N)+mu*MassTerm(N),N)
            #  omega=linalg.eigs(W, k=2, which='SR', return_eigenvectors=False)
            omegaprime=linalg.eigs(Wprime, k=2, which='SR', return_eigenvectors=False)

            #print(np.real(omega), np.real(omegaprime), "\n\n")
            print(Volume, y, np.real(omegaprime[1]/(2*N)*y**2), np.real(-0.5*(omegaprime[1]-omegaprime[0])*y))
    print('%\n')

def M1durchgV2 (mdurchg):
    for eta in range(30,150,5):
        y=eta/100
        for N in range(4, 25, 2):
            mu=2*mdurchg/y
            if mu !=0:
                omegaprime=linalg.eigs(NonZeroSpin_entferner(V(N)/(y**2)+WL(N)+mu*MassTerm(N),N), k=2, which='SR', return_eigenvectors=False)
            else:
                omegaprime=linalg.eigs(NonZeroSpin_entferner(V(N)/(y**2)+WL(N),N), k=2, which='SR', return_eigenvectors=False)
            print(y, N, np.real(-0.5*(omegaprime[1]-omegaprime[0])*y), np.real(0.5*omegaprime[0]*y**2/N))
    print('%\n')

def Grundzustand (mdurchg):
    for Volume in range(5,21,5):
        for N in range(4, 25, 2):
            y=Volume/N
            mu=2*mdurchg/y

            #W=V(N)/(y**2)+WL(N)
            Wprime=NonZeroSpin_entferner(V(N)/(y**2)+WL(N)+mu*MassTerm(N),N)
            #  omega=linalg.eigs(W, k=2, which='SR', return_eigenvectors=False)
            omegaprime=linalg.eigs(Wprime, k=1, which='SR', return_eigenvectors=False)

            #print(np.real(omega), np.real(omegaprime), "\n\n")
            print(Volume, y, np.real(0.5*omegaprime[0]*y**2/N))
    print('\n')

def GrundzustandV2 (mdurchg):
    for eta in range(2,11,2):
        y=eta/10
        for N in range(4, 25, 2):
            mu=2*mdurchg/y
            #W=V(N)/(y**2)+WL(N)
            if mu !=0:
                Wprime=NonZeroSpin_entferner(V(N)/(y**2)+WL(N)+mu*MassTerm(N),N)
            else:
                Wprime=NonZeroSpin_entferner(V(N)/(y**2)+WL(N),N)
            #  omega=linalg.eigs(W, k=2, which='SR', return_eigenvectors=False)
            omegaprime=linalg.eigs(Wprime, k=1, which='SR', return_eigenvectors=False)

            #print(np.real(omega), np.real(omegaprime), "\n\n")
            print(y, N, np.real(0.5*omegaprime[0]*y**2/N))
    print('\n')


def Dispersion (N,x,mdurchg):
    K=20 #anzahl energien
    mu=2*mdurchg*np.sqrt(x)

    #Hprime=NonZeroSpin_entferner(V(N)*x+WL(N)+mu*MassTerm(N),N)
     
    omega=linalg.eigs(V(N)*x+WL(N)+mu*MassTerm(N)+4*S(N)@S(N), k=K, which='SR', return_eigenvectors=True)
    omegaprime=linalg.eigs(NonZeroSpin_entferner(V(N)*x+WL(N)+mu*MassTerm(N),N), k=K, which='SR', return_eigenvectors=True)

    Op2=-Op(N,x)@Op(N,x)
    Op2_prime=NonZeroSpin_entferner(-Op(N,x)@Op(N,x),N)
    SRprime=NonZeroSpin_entferner(SR(N), N)
    #SR2prime=NonZeroSpin_entferner(SR2(N), N)

    #E=np.real(omega[0])
    Eprime=np.real(omegaprime[0])
    E=np.real(omega[0])
    for i in range(0,K):
        #print(E[i],np.real(Herm(omega[1][:,i])@Op2@omega[1][:,i]) , Herm(omega[1][:,i])@Sr@omega[1][:,i], Eprime[i], np.real(Herm(omegaprime[1][:,i])@Op2_prime@omegaprime[1][:,i]), Herm(omegaprime[1][:,i])@SRprime@omegaprime[1][:,i])
        print(Eprime[i], E[i], np.real(Herm(omegaprime[1][:,i])@Op2_prime@omegaprime[1][:,i]), np.real(Herm(omega[1][:,i])@Op2@omega[1][:,i]), Herm(omegaprime[1][:,i])@SRprime@omegaprime[1][:,i], Herm(omega[1][:,i])@SR(N)@omega[1][:,i]) 

def Phase (N,x,mdurchg):
    K=20 #anzahl energien
    mu=2*mdurchg*np.sqrt(x)

    omegaprime=linalg.eigs(NonZeroSpin_entferner(V(N)*x+WL(N)+mu*MassTerm(N),N), k=K, which='SR', return_eigenvectors=True)

    SRprime=NonZeroSpin_entferner(SR(N), N)

   # phase=omega[1].getH()@Sr@omega[1]
    #phase_prime=omegaprime[1].getH()@SRprime@omegaprime[1]

    #E=np.real(omega[0])
    Eprime=np.real(omegaprime[0])

    for i in range(0,K):
        print(Eprime[i], np.real(Herm(omegaprime[1][:,i])@Op2_prime@omegaprime[1][:,i])) # Herm(omegaprime[1][:,i])@SRprime@omegaprime[1][:,i])

def Skalar(mdurchg):
    for eta in range(30,150,5):
        y=eta/100
        for N in range(10, 25, 2):
            K=8
            mu=2*mdurchg/y
            if mu !=0:
                omegaprime=linalg.eigs(NonZeroSpin_entferner(V(N)/(y**2)+WL(N)+mu*MassTerm(N),N), k=K, which='SR', return_eigenvectors=True)
            else:
                omegaprime=linalg.eigs(NonZeroSpin_entferner(V(N)/(y**2)+WL(N),N), k=K, which='SR', return_eigenvectors=True)
            
            SRprime=NonZeroSpin_entferner(SR(N), N)
            Eprime=np.real(omegaprime[0])

            for i in range(4,K):
                if np.real(Herm(omegaprime[1][:,i])@SRprime@omegaprime[1][:,i])>0:
                    scalar=i
                    i+=K     
            
            print(y, N, np.real(0.5*(Eprime[1]-Eprime[0])*y), np.real(0.5*Eprime[0]*y**2/N), np.real(-0.5*(Eprime[0]-Eprime[scalar])*y))



Skalar(0)


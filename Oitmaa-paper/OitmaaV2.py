from deco import concurrent, synchronized
import numpy as np
from scipy.sparse import *
#from multiprocessing import Process
import ast
import time

dense_matrix = np.array([[0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]])

h = csr_matrix(dense_matrix)



sigmax=csr_matrix(np.array([[0,1],[1, 0]]))
sigmaz=csr_matrix(np.array([[1,0],[0,-1]]))
sigmap=csr_matrix(np.array([[0,1],[0,0]]))
sigmam=csr_matrix(np.array([[0,0],[1,0]]))

#Daten fuer Renormierung
with open('MS_Vol.dat') as f:
    data = f.read()
dictVol = ast.literal_eval('{'+data+'}')

with open('dictionary2.txt') as f:
    data = f.read()
dict = ast.literal_eval(data)

#Terme des Hamiltonians
def Herm (A):
    return np.conjugate(np.transpose(A))

def Inter (n,M,l):
    A=kron(sigmaz-eye_array(2),eye_array(2**(M-1)))+2*eye_array(2**M)*l
   # print(0, "\n", A)
    for  k in range(2, n+1):
        xi=kron(eye_array(2**(k-1)), sigmaz+(-1)**k*eye_array(2))
        #print(1, k,"\n",xi)#, eye_array(2**(M-k))))
        A+=kron(xi, eye_array(2**(M-k)))
        #print(A)
        #A+=kron(eye_array(2**(k-1)), sigmaz+(-1)**k*eye_array(2), eye_array(2**(M-k)))
    A=A@A/4
    return A;

def L_n(N,n,l=0):
    if n==0:
        return eye_array(2**N)*l
    else:
        A=kron(sigmaz-eye_array(2),eye_array(2**(N-1)))+eye_array(2**N)*l*2
        for  k in range(2, n+1):
            xi=kron(eye_array(2**(k-1)), sigmaz+(-1)**k*eye_array(2))
            A+=kron(xi, eye_array(2**(N-k)))
    return 0.5*A

def Q_n(N,n):
    if n==1:
        A=kron(sigmaz-eye_array(2),eye_array(2**(N-1)))
    elif n==N:
        A=kron(eye_array(2**(N-1)),sigmaz+eye_array(2))
    else:
        xi=kron(eye_array(2**(n-1)), sigmaz+(-1)**n*eye_array(2))
        A=kron(xi, eye_array(2**(N-n)))
    return 0.5*A

def WL(M,l=0):
    A=Inter(1,M,l)
    for n in range(2,M):
        A+=Inter(n,M,l)
    return A

def Foverg(M,l,n_start, xi):
    A=L_n(M,n_start,l)
    for i in range(n_start+1,n_start+xi+1):
        tmp=kron(eye_array(2**(i-1)), sigmaz+(-1)**i*eye_array(2))
        A+=0.5*(1-(i-n_start)/(xi+1))*kron(tmp, eye_array(2**(M-i)))
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

def ChiralCondensate_overg(N,y):
    summand=eye_array(2)+sigmaz
    A=-1*kron(summand,eye_array(2**(N-1)))
    for i in range(2,N):
        xi=kron(summand, eye_array(2**(N-i)))*(-1)**i
        A+=kron(eye_array(2**(i-1)), xi)
    A+=kron(eye_array(2**(N-1)),summand)
    return A/(2*N*y)

def Free_Condensate_overg(moverg, y, N):
    mu=2*moverg/y
    x=1/(y**2)
    A=0
    for q in range(1, int(N/2)+1):
        A+=mu/np.sqrt(mu**2+4*x**2*(np.cos(q*np.pi/(N+1)))**2)
    return A/(N*y)

def Dispersion (N,x,mdurchg, l0):
    K=15 #anzahl energien
    mu=2*mdurchg*np.sqrt(x)
    #omega=linalg.eigs(V(N)*x+WL(N, l0)+mu*MassTerm(N)+4*S(N)@S(N), k=K, which='SR', return_eigenvectors=True)
    omegaprime=linalg.eigs(NonZeroSpin_entferner(V(N)*x+WL(N,l0)+mu*MassTerm(N),N), k=K, which='SR', return_eigenvectors=True)

    Op2_prime=NonZeroSpin_entferner(-Op(N,x)@Op(N,x),N)
    SRprime=NonZeroSpin_entferner(SR(N), N)
    #SR2prime=NonZeroSpin_entferner(SR2(N), N)

    #E=np.real(omega[0])
    Eprime=np.real(omegaprime[0])
    #E=np.real(omega[0])
    for i in range(0,K):
        print(Eprime[i], np.real(Herm(omegaprime[1][:,i])@Op2_prime@omegaprime[1][:,i]), np.real(Herm(omegaprime[1][:,i])@SRprime@omegaprime[1][:,i])) 

def Phase (N,x,mdurchg):
    K=20 #anzahl energien
    mu=2*mdurchg*np.sqrt(x)
    omegaprime=linalg.eigs(NonZeroSpin_entferner(V(N)*x+WL(N)+mu*MassTerm(N),N), k=K, which='SR', return_eigenvectors=True)
    SRprime=NonZeroSpin_entferner(SR(N), N)
    Eprime=np.real(omegaprime[0])

    for i in range(0,K):
        print(Eprime[i], np.real(Herm(omegaprime[1][:,i])@Op2_prime@omegaprime[1][:,i])) # Herm(omegaprime[1][:,i])@SRprime@omegaprime[1][:,i])

def SkalarV2(mdurchg,l0):
    for eta in range(500,1200,100):
        y=eta/1000
        for N in range(10, 25, 2):
            K=18
            mu=2*mdurchg/y
            if mu !=0:
                omegaprime=linalg.eigs(NonZeroSpin_entferner(V(N)/(y**2)+WL(N,l0)+mu*MassTerm(N),N), k=K, which='SR', return_eigenvectors=True)
            else:
                omegaprime=linalg.eigs(NonZeroSpin_entferner(V(N)/(y**2)+WL(N,l0),N), k=K, which='SR', return_eigenvectors=True)
            
            SRprime=NonZeroSpin_entferner(SR(N), N)
            Eprime=np.real(omegaprime[0])

            scalar=0
            i=2
            while scalar==0:
                #print(Herm(omegaprime[1][:,i])@SRprime@omegaprime[1][:,i])
                if np.real(Herm(omegaprime[1][:,i])@SRprime@omegaprime[1][:,i])>0:
                    scalar=i
                i=i+1 

            return [np.real(0.5*(Eprime[1]-Eprime[0])*y), np.real(0.5*Eprime[0]*y**2/N), np.real(-0.5*(Eprime[0]-Eprime[scalar])*y)]
            #print(mdurchg, y, N, np.real(0.5*(Eprime[1]-Eprime[0])*y), np.real(0.5*Eprime[0]*y**2/N), np.real(-0.5*(Eprime[0]-Eprime[scalar])*y), scalar)
    #print("%")

#@concurrent
def Skalar(mdurchg, N, y, l0):
    K=20
    mu=2*mdurchg/y
    omegaprime=linalg.eigs(NonZeroSpin_entferner(V(N)/(y**2)+WL(N,l0)+mu*MassTerm(N),N), k=K, which='SR', return_eigenvectors=True)
    SRprime=NonZeroSpin_entferner(SR(N), N)
    Eprime=np.real(omegaprime[0])
    x=1/(y*y)
    Op2_prime=NonZeroSpin_entferner(-Op(N,x)@Op(N,x),N)
    scalar=0
    i=2
    while scalar==0:
        if np.real(Herm(omegaprime[1][:,i])@SRprime@omegaprime[1][:,i])>0:
            scalar=i
        i=i+1
    P=[] 
    scalar2=0
    for j in range(0,K):
        #if scalar2==0:
        P.append(np.real(Herm(omegaprime[1][:,j])@Op2_prime@omegaprime[1][:,j]))
        if j>2 and  P[j] < P[2] and scalar2==0:
            scalar2=j
		
    return [np.real(0.5*(Eprime[1]-Eprime[0])*y), np.real(0.5*Eprime[0]*y**2/N), np.real(-0.5*(Eprime[0]-Eprime[scalar])*y), np.real(-0.5*(Eprime[0]-Eprime[scalar2])*y)]   
    #print(mdurchg, Vol, y, np.real(0.5*(Eprime[1]-Eprime[0])*y), np.real(0.5*Eprime[0]*y**2/N), np.real(-0.5*(Eprime[0]-Eprime[scalar])*y), scalar)

#@synchronized
def SkalarV2ren(mdurchg,l0):
    ys=[]
    Ns=[]
    Es=[]
    for eta in range(300,1001,50):
        y=eta/1000
        for N in range(10, 25, 2):
            ys.append(y)
            Ns.append(N)
            Es.append(Skalar(mdurchg-Renormierung(N,y,l0),N,y, l0))
    for i in range(0,len(ys)):
        print(mdurchg,ys[i], Ns[i], Es[i][0], Es[i][1], Es[i][2], Es[i][3] , l0, flush=True)

#@synchronized
def SkalarVolren(Vol,mdurchg,l0):
    ys=[]
    Ns=[]
    Es=[]
    for N in range(10, 29, 2):
            y=Vol/N
            ys.append(y)
            Ns.append(N)
            Es.append(Skalar(mdurchg-RenormierungVol(Vol,N,l0),N,y, l0))
    for i in range(0,len(ys)):
        print(mdurchg,Vol, ys[i], Es[i][0], Es[i][1], Es[i][2], Es[i][3] , l0, Ns[i], flush=True)
        

        

def Skalarren(Vol, mdurchg, l0):
        for N in range(10, 27, 2):
            K=15
            y=Vol/N
            mu=2*mdurchg/y-2*RenormierungVol(Vol, N, l0)/y
            if mu !=0:
                omegaprime=linalg.eigs(NonZeroSpin_entferner(V(N)/(y**2)+WL(N, l0)+mu*MassTerm(N),N), k=K, which='SR', return_eigenvectors=True)
            else:
                omegaprime=linalg.eigs(NonZeroSpin_entferner(V(N)/(y**2)+WL(N, l0),N), k=K, which='SR', return_eigenvectors=True)
            
            #SRprime=NonZeroSpin_entferner(SR(N), N)
            Eprime=np.real(omegaprime[0])
            x=1/(y*y)
            Op2_prime=NonZeroSpin_entferner(-Op(N,x)@Op(N,x),N)
            scalar=0
            #i=2
            #while scalar==0:
                #print(Herm(omegaprime[1][:,i])@SRprime@omegaprime[1][:,i])
                #if np.real(Herm(omegaprime[1][:,i])@SRprime@omegaprime[1][:,i])>0:
                    #scalar=i
                #i=i+1 
            P=[] 
            scalar2=0
            for j in range(0,K):
                if scalar2==0:
                    P.append(np.real(Herm(omegaprime[1][:,j])@Op2_prime@omegaprime[1][:,j]))
                if scalar2==0:
                    if j>2 and  P[j] < P[2] and scalar2==0:
                        scalar2=j
            #print(P)
            print(mdurchg, Vol, y, np.real(0.5*(Eprime[1]-Eprime[0])*y), np.real(0.5*Eprime[0]*y**2/N), np.real(-0.5*(Eprime[0]-Eprime[scalar])*y), np.real(-0.5*(Eprime[0]-Eprime[scalar2])*y), l0, flush=True)
            #print(mdurchg, Vol, y, np.real(0.5*(Eprime[1]-Eprime[0])*y), np.real(0.5*Eprime[0]*y**2/N), np.real(-0.5*(Eprime[0]-Eprime[scalar2])*y), l0, flush=True)

@synchronized
def ComputeStringtension(mdurchg, alpha):
    Sts=[[0]*5]*11*8
    for eta in range(100,151,5):
        for N in range(10, 25, 2):
            Sts[int((N-10)/2+8*(eta-100)/5)]=Stringtension(N,eta/100,mdurchg, alpha)

    for i in range(0, len(Sts)):
         print(mdurchg, alpha, Sts[i][0], Sts[i][1], Sts[i][2], Sts[i][3], Sts[i][4])	

@synchronized
def ComputeStringtensionVol(Vol,mdurchg, alpha, Nmin=10, Nmax=26):
    Sts=[[0]*5]*9
    for N in range(Nmin, Nmax+1, 2):
        Sts[int((N-Nmin)/2)]=StringtensionVol(N,Vol,mdurchg, alpha)

    for i in range(0, len(Sts)):
         print(mdurchg, alpha, Sts[i][0], Sts[i][1], Sts[i][2], Sts[i][3], Sts[i][4])	

@concurrent
def StringtensionVol(N,Vol,mdurchg,alpha):
            y=Vol/N
            mu=2*(mdurchg-RenormierungVol(Vol,N,alpha))/y
            omega0=np.real(linalg.eigs(NonZeroSpin_entferner(V(N)/(y**2)+WL(N)+mu*MassTerm(N),N), k=1, which='SR', return_eigenvectors=False))
            omegaAlpha=np.real(linalg.eigs(NonZeroSpin_entferner(V(N)/(y**2)+WL(N,alpha)+mu*MassTerm(N),N), k=1, which='SR', return_eigenvectors=False))
            #print(mdurchg, alpha, y, N, omega0[0], omegaAlpha[0], (omegaAlpha[0]-omega0[0])/N)
            return [y, N, omega0[0], omegaAlpha[0], (omegaAlpha[0]-omega0[0])/N]

@concurrent
def Stringtension(N,y,mdurchg,alpha):
            mu=2*(mdurchg-Renormierung(N,y,alpha))/y
            omega0=np.real(linalg.eigs(NonZeroSpin_entferner(V(N)/(y**2)+WL(N)+mu*MassTerm(N),N), k=1, which='SR', return_eigenvectors=False))
            omegaAlpha=np.real(linalg.eigs(NonZeroSpin_entferner(V(N)/(y**2)+WL(N,alpha)+mu*MassTerm(N),N), k=1, which='SR', return_eigenvectors=False))
            #print(mdurchg, alpha, y, N, omega0[0], omegaAlpha[0], (omegaAlpha[0]-omega0[0])/N)
            return [y, N, omega0[0], omegaAlpha[0], (omegaAlpha[0]-omega0[0])/N]


@concurrent
def MassShift(N,y,l0,m0,stepsize=0.05):
    #iteriere ueber Massen
    threshold=0.001
    Massen=[]
    Felder=[]
    Massen.append(m0) 
    Felder.append(Erwartungswert_Foverg(N,y,l0,m0))

    if Felder[0]>0 and l0<0.5 or Felder[0]<0 and l0>0.5 :
        s=-stepsize
    else:
        s=stepsize
    n=1
    Massen.append(m0+n*s)
    Felder.append(Erwartungswert_Foverg(N,y,l0,Massen[n]))

    if np.sign(Felder[0]*Felder[1]) > 0 and np.abs(Felder[1])>np.abs(Felder[0]):
        s=-s
    while np.sign(Felder[0]*Felder[n]) > 0: 
        #print(Massen[n], Felder[n])

        n=n+1
        Massen.append(m0+n*s)
        Felder.append(Erwartungswert_Foverg(N,y,l0,Massen[n]))
    i=0
    direction=np.sign(Massen[n]-Massen[n-1])
    while(np.abs(s)>threshold):
        #print(Massen[n+i], Felder[n+i])

        s=stepsize*2**(-(i+1))

        if np.sign(Felder[n+i]*Felder[n+i-1])<0:
            direction=-direction

        Massen.append(Massen[n+i]+s*direction) 
        i+=1
        Felder.append(Erwartungswert_Foverg(N,y,l0,Massen[n+i]))

    p=np.polyfit(Massen[n+2:n+i],Felder[n+2:n+i],2)
    
    MSoptions=[(-p[1]-np.sqrt(p[1]**2-4*p[2]*p[0]))/(2*p[0]),(-p[1]+np.sqrt(p[1]**2-4*p[2]*p[0]))/(2*p[0])] #NST des Polynoms
    MS= MSoptions[np.argmin(np.abs(MSoptions-Massen[n+i]))] #Finde die, die naeher am letzten Wert liegt
    #print(p,MSoptions, MS, "\n")
    return -MS
   

@synchronized
def MassShiftVol(Vol, l0, Nmax=24, Nmin=10, stepsize=0.2):
	ys=[]
	Ns=[]
	MSs=[]
	for N in range(Nmin, Nmax+1,2):
		ys.append(Vol/N)
		m0=-1.3*Vol/N
		Ns.append(N)
		MSs.append(MassShift(N,Vol/N,l0,m0, stepsize))
	for i in range(0, len(ys)):
		print("\""+str(Vol)+"_"+str(Ns[i])+"_"+str(l0)+"\":", MSs[i], ",", flush=True)

def Erwartungswert_Foverg(N,y,l0,mdurchg):      
    mu=2*mdurchg/y
    omega0=linalg.eigs(NonZeroSpin_entferner(V(N)/(y**2)+WL(N,l0)+mu*MassTerm(N),N), k=1, which='SR', return_eigenvectors=True)
    Fdurchg=np.real(Herm(omega0[1][:,0])@NonZeroSpin_entferner(Foverg(N,l0,int(N/2),1),N)@omega0[1][:,0])
    return Fdurchg
    

def EwLadung(N,y,l0,mdurchg):
    mu=2*mdurchg/y
    omega0=linalg.eigs(NonZeroSpin_entferner(V(N)/(y**2)+WL(N,l0)+mu*MassTerm(N),N), k=1, which='SR', return_eigenvectors=True)
    for k in range(1, N+1):
        print(k, 
        np.real(Herm(omega0[1][:,0])@NonZeroSpin_entferner(Q_n(N,k),N)@omega0[1][:,0]), 
        np.real(Herm(omega0[1][:,0])@NonZeroSpin_entferner(L_n(N,k-1,l0),N)@omega0[1][:,0]),
        0.5*(np.real(Herm(omega0[1][:,0])@NonZeroSpin_entferner(L_n(N,k,l0),N)@omega0[1][:,0])+\
            np.real(Herm(omega0[1][:,0])@NonZeroSpin_entferner(L_n(N,k-1,l0),N)@omega0[1][:,0])))    
    


@synchronized
def ComputeMassShift(l0, Nmax=22, Nmin=10):
    etas=list(range(100,151,5))
    Ns=list(range(Nmin,Nmax+1,2))
    MSs=[0]*len(Ns)*len(etas)

    for eta in etas:
        for N in Ns:  
            MSs[int((N-Ns[0])/2+len(Ns)*(eta-etas[0])/5)]=MassShift(N,eta/100,l0,-0.125*eta/100,0.15)

    for j in range(0,len(etas)):
        for i in range(0,len(Ns)):
             print("\""+str(Ns[i])+"_"+str(etas[j]/100)+"_"+str(l0)+"\":", MSs[int((Ns[i]-Ns[0])/2+len(Ns)*(etas[j]-etas[0])/5)], ",", flush=True)
          

#bussje
@synchronized
def ComputeMassShift_Abh_l(N,y):
	ls=[]
	MSs=[]
	for L in range(10,496,20):
			l=L/1000  
			m0=-0.13*y
			MSs.append(MassShift(N,y,l,m0,0.15))
			ls.append(l)
	for i in range(0,int(len(ls))):
		print(ls[i], MSs[i], 8*MSs[i]/y, ls[len(ls)-i-1], MSs[len(ls)-i-1], MSs[i]/MSs[len(ls)-i-1],  flush=True)


def RenormierungVol(Vol, N, l0):
    return dictVol[str(Vol)+"_"+str(N)+"_"+str(l0)]

def Renormierung(N,y,l0):
	return dict[str(N)+"_"+str(y)+"_"+str(l0)]
	
@concurrent
def EW_Condensate(moverg, l0, N,y): 
    mu=2*moverg/y
    omega0=linalg.eigs(NonZeroSpin_entferner(V(N)/(y**2)+WL(N,l0)+mu*MassTerm(N),N), k=1, which='SR', return_eigenvectors=True)
    Condensate=np.real(Herm(omega0[1][:,0])@NonZeroSpin_entferner(ChiralCondensate_overg(N,y),N)@omega0[1][:,0])
    return [Condensate, Free_Condensate_overg(moverg,y,N), Condensate-Free_Condensate_overg(moverg,y,N)]

@synchronized
def ComputeCondensate(Vol,mdurchg, alpha, Nmin=10, Nmax=26):
    CCs=[0*3]*9
    Ns=list(range(Nmin, Nmax+1, 2))
    for N in range(Nmin, Nmax+1, 2):
        y=Vol/N
        CCs[int((N-Nmin)/2)]=EW_Condensate(mdurchg-RenormierungVol(Vol,N,alpha), alpha, N,y)

    for i in range(0, len(Ns)):
         print(Ns[i], Vol,mdurchg, alpha, CCs[i][0], CCs[i][1], CCs[i][2])	

ComputeCondensate(25,0,0.25, 10,20)
import ast
import numpy as np
import matplotlib.pyplot as plt

with open('MS_Vol.dat') as f:
    data = f.read()
dictVol = ast.literal_eval('{'+data+'}')

with open('MS_AllesMoegliche_N_y_l.dat') as f:
    data = f.read()
dict = ast.literal_eval('{'+data+'}')

def RenormierungVol(Vol, N, l0):
    return dictVol[str(Vol)+"_"+str(N)+"_"+str(l0)]

def Renormierung(N,y,l0):
	return dict[str(N)+"_"+str(y)+"_"+str(l0)]


def extrapolVol(Vol,N, Ls):
    MSs=[]
    for l in Ls:
        MSs.append(N*RenormierungVol(Vol,N,l)/Vol)
    plt.plot(Ls,MSs, linestyle='--', marker='.', markersize=10, label=str(N))

x=np.linspace(0,0.5,1000)
a=0.045
Ls=[0.05, 0.1, 0.2, 0.3, 0.4, 0.45, 0.475, 0.485, 0.495]
for N in range(10, 27,40):
    extrapolVol(25,N, Ls)
    plt.plot(x,0.125+a*np.cos(2*np.pi*x))


plt.legend(loc="lower left",handletextpad=-0.5, borderpad=0.4)
plt.show()
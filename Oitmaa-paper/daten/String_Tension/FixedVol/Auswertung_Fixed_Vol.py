import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline


plt.rcParams['text.usetex'] = True
plt.rcParams.update({'font.size': 15})

def Extrapolator(m,l,deg=2,PLOT=0):
    NumN=8
    
    FR=[3, NumN]

    Data=np.loadtxt('ST_Vol25_zentrum_m'+m+'_l'+l+'.dat')

    N=Data[FR[0]:FR[1], 0]
    #Y=Data[FR[0]:FR[1], 6]
    ST=Data[FR[0]:FR[1], 6]

    Np=Data[0:NumN, 0]
    STp=Data[0:NumN, 6]
    #print(1/N, ST)

    p,cov=np.polyfit(1/N, ST, deg, cov=True)
    #print(p[deg], end=" ")
    x=np.linspace(0,0.11,1000)

    STextrapol=0*x

    for i in range(0,deg+1):
        STextrapol+=p[i]*x**(deg-i)


    if PLOT==1:
        plt.plot(x, STextrapol)
        plt.plot(1/Np,STp, '.', markersize=10)
        plt.xlim(0,0.1)
        plt.show()

    
    return([p[deg],np.sqrt(np.diag(cov)[deg])])

Extrapolator("0.2", "0.49",2,1)

x=np.linspace(0,1,1000)
x1=np.linspace(0.05,0.5,1000)


plt.plot(x,x**2, color='black')
ls=[0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.475, 0.485, 0.49, 0.5]#, 0.515, 0.525, 0.55, 0.6, 0.7, 0.8, 0.9, 0.95]
Ms=[0, 0.05, 0.1, 0.2,0.3, 0.35, 0.4, 0.8, 1.6]
STs=np.zeros((len(Ms), len(ls)))
Err=np.zeros((len(Ms), len(ls)))
STs2=np.zeros((len(Ms), len(ls)))
Err2=np.zeros((len(Ms), len(ls)))

plt.gca().set_prop_cycle(None)
for i in range(0,len(Ms)):
    for j in range(0,len(ls)):
        print(str(Ms[i]), str(ls[j]))
        STs[i][j],Err[i][j]=Extrapolator(str(Ms[len(Ms)-1-i]), str(ls[j]),2, 0)
#       STs2[i][j],Err2[i][j]=Extrapolator(str(Ms[i]), str(ls[j]),3, 0)

    #plt.plot(ls, STs[i,:], linestyle='--', marker='.', markersize=10,  label=str(Ms[i]))#linewidth=1,
    plt.errorbar(ls, STs[i,:], Err[i,:],linestyle='', marker='.', markersize=10)#,  label=str(Ms[i]))
    
plt.gca().set_prop_cycle(None)
for i in range(0,len(Ms)):
    X_Y_Spline = make_interp_spline(ls,STs[i,:]) 
    plt.plot(x,X_Y_Spline(x), linestyle='--')

plt.gca().set_prop_cycle(None)
for i in range(0,len(Ms)):
    plt.plot(-5,0.1, marker='.', linestyle='', markersize=8, label=str(Ms[len(Ms)-1-i]))

#plt.plot(x,0*x, color='black')
plt.xlim(0,0.5)
plt.ylim(-0.02,0.25)

plt.legend(loc="upper left",handletextpad=-0.5, borderpad=0.4)

plt.xlabel('$l_0$',  fontsize=17)
plt.ylabel('$\\frac{2T}{g^2}$', fontsize=17, rotation=0)
plt.plot(x,0*x, '--', color='black')
plt.show()    
#print(STs)


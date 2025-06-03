import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True
plt.rcParams.update({'font.size': 15})

def Extrapolator(m,l,deg=2,PLOT=0):
    NumN=9
    
    FR=[4, NumN]

    Data=np.loadtxt('ST_Vol25_m'+m+'_l'+l+'.dat')

    N=Data[FR[0]:FR[1], 3]
    Y=Data[FR[0]:FR[1], 3]
    ST=Data[FR[0]:FR[1], 6]

    Np=Data[0:NumN, 3]
    STp=Data[0:NumN, 6]
    #print(1/N, ST)

    p,cov=np.polyfit(25/N, ST, deg, cov=True)
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


x=np.linspace(0,0.5,1000)

plt.plot(x,x**2, color='black')
ls=[0.05, 0.1, 0.2, 0.3, 0.4, 0.45, 0.475, 0.485, 0.495]
Ms=[0, 0.05, 0.1, 0.2, 0.4, 0.8, 1.6]
STs=np.zeros((len(Ms), len(ls)))
Err=np.zeros((len(Ms), len(ls)))
STs2=np.zeros((len(Ms), len(ls)))
Err2=np.zeros((len(Ms), len(ls)))

for i in range(0,len(Ms)):
    for j in range(0,len(ls)):
        #print(str(Ms[i]), str(ls[j]))
        STs[i][j],Err[i][j]=Extrapolator(str(Ms[i]), str(ls[j]), 0)
        STs2[i][j],Err2[i][j]=Extrapolator(str(Ms[i]), str(ls[j]),3, 0)

    #plt.plot(ls, STs[i,:], linestyle='--', marker='.', markersize=10,  label=str(Ms[i]))#linewidth=1,
    plt.errorbar(ls, STs2[i,:], Err2[i,:], linestyle='--', marker='.', markersize=10,  label=str(Ms[i]))

#plt.plot(x,0*x, color='black')
plt.xlim(0,0.5)

plt.legend(loc="upper left")

plt.xlabel('$l_0$',  fontsize=17)
plt.ylabel('$\\frac{2T}{g^2}$', fontsize=17, rotation=0)
plt.show()    
#print(STs)


import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True
plt.rcParams.update({'font.size': 15})

ColN=0
ColY=1
ColObs=6

deg1=3
Fit1Range=list(range(2,8))
deg2=2
Fit2Range=list(range(0,8))

degA=1
FitARange=list(range(2,6))

NumN=8
etas=list(range(80,136,5))
#etas=list(range(30,91,10))

NumY=len(etas)

#Data=np.loadtxt('ST_Vol25_m'+m+'_l'+l+'.dat')
#Data=np.loadtxt('testdata')

def extrapolN(y,Data, plot=0):
    #print(Data)
    indicesY=np.where(Data[:,ColY]==y)[0]
    #print(indicesY)
    #Data2=Data[indicesY[0]:indicesY[len(indicesY)-1],:]
    Data2=Data[indicesY, :]

    p,cov=np.polyfit(1/Data2[Fit1Range,ColN], Data2[Fit1Range,ColObs],deg1, cov=True)

    if plot==1:
        x=np.linspace(0,0.1,1000)
        Obsfit=0*x
        for i in range(0,deg1+1):
            Obsfit+=p[deg1-i]*x**(i)
        plt.plot(x,Obsfit)
        plt.plot(1/Data2[:,ColN], Data2[:,ColObs], '.')
        plt.title("y="+str(y))
        plt.show()
    #print(p, cov)
    return [p[deg1], np.sqrt(cov[deg1, deg1])]


def Aitken(y,Data, plot=0):
    indicesY=np.where(Data[:,ColY]==y)[0]
    #print(indicesY)
    #Data2=Data[indicesY[0]:indicesY[len(indicesY)-1],:]
    N=Data[indicesY, ColN]
    X_N=Data[indicesY, ColObs]
    A=[]
    N2=[]
    for n in range(0, NumN-2):
        x_n=X_N[n]
        delta_x_n=X_N[n+1]-x_n
        delta_sq_x_n=x_n-2*X_N[n+1]+X_N[n+2]
        A.append(x_n-(delta_x_n**2)/delta_sq_x_n)
        N2.append(N[n])

    
    p,cov=np.polyfit(1/N, X_N,deg1, cov=True)
    p2,cov2=np.polyfit(1/np.array(N2[FitARange[0]:FitARange[-1]]), A[FitARange[0]:FitARange[-1]],degA, cov=True)
    if plot==1:
        x=np.linspace(0,0.1,1000)
        Obsfit=0*x
        Obsfit2=0*x
        for i in range(0,deg1+1):
            Obsfit+=p[deg1-i]*x**(i)
        for i in range(0,degA+1):
            Obsfit2+=p2[degA-i]*x**(i)
        plt.plot(x,Obsfit)
        plt.plot(1/N, X_N, '.')
        plt.plot(x,Obsfit2, label='Aitken')
        plt.plot(1/np.array(N2), A, '.')

        plt.title("y="+str(y))
        plt.show()
    #print(p, cov)
    #return [p2[degA], np.sqrt(cov2[degA, degA])]
    return [0.333*(2*A[-1]+A[-2]), np.sqrt(np.abs(0.5*((A[-1]-A[-2]))))]

def extrapoly(Data,plot=0):
    #print(Data)
    ys=[]
    Obs_infVol_y_s=[]
    errs=[]
    weights=[]
    #Obs_infVol_y=[]*NumY
    errs=[]*NumY
    for eta in etas:
        y=eta/100
        ys.append(y)
        Obs_infVol_y,err=extrapolN(y,Data)
        #Obs_infVol_y,err=Aitken(y,Data)
        Obs_infVol_y_s.append(Obs_infVol_y)
        errs.append(err)
        weights.append(1/err)

    p,cov=np.polyfit(ys[Fit2Range[0]:Fit2Range[-1]], Obs_infVol_y_s[Fit2Range[0]:Fit2Range[-1]], deg2, w=weights[Fit2Range[0]:Fit2Range[-1]], cov=True)
    if plot==1:
        x=np.linspace(0,1.5,1000)
        Obsfit=0*x
        for i in range(0,deg2+1):
            Obsfit+=p[deg2-i]*x**(i)
        plt.plot(x,Obsfit)
        plt.errorbar(ys,Obs_infVol_y_s, errs,linestyle='', marker='.', markersize=10)
        plt.show()
    #print(p, p[deg2])
    return [p[deg2], np.sqrt(cov[deg2, deg2])]

def extrapolyA(Data,plot=0):
    #print(Data)
    ys=[]
    Obs_infVol_y_s=[]
    errs=[]
    weights=[]
    #Obs_infVol_y=[]*NumY
    errs=[]*NumY
    for eta in etas:
        y=eta/100
        ys.append(y)
        #Obs_infVol_y,err=extrapolN(y,Data)
        Obs_infVol_y,err=Aitken(y,Data)
        Obs_infVol_y_s.append(Obs_infVol_y)
        errs.append(err)
        weights.append(1/err)

    p,cov=np.polyfit(ys[Fit2Range[0]:Fit2Range[-1]], Obs_infVol_y_s[Fit2Range[0]:Fit2Range[-1]], deg2, w=weights[Fit2Range[0]:Fit2Range[-1]], cov=True)
    if plot==1:
        x=np.linspace(0,1.5,1000)
        Obsfit=0*x
        for i in range(0,deg2+1):
            Obsfit+=p[deg2-i]*x**(i)
        plt.plot(x,Obsfit)
        plt.errorbar(ys,Obs_infVol_y_s, errs,linestyle='', marker='.', markersize=10)
        plt.show()
    #print(p, p[deg2])
    return [p[deg2], np.sqrt(cov[deg2, deg2])]

#extrapolN(1,Data,1)
#extrapoly(plot=1)



Masses=[0, 0.05, 0.1, 0.2, 0.3, 0.35, 0.4, 0.8, 1.6]
ls=[0.05, 0.1, 0.15,0.2, 0.25,0.3, 0.35, 0.4, 0.45, 0.475, 0.5]

STs=np.zeros((len(Masses), len(ls)))
Errs=np.zeros((len(Masses), len(ls)))

Data=np.loadtxt('ST_V2_zentrum_m'+str(0)+'_l'+str(0.2)+'.dat')

#print(Data)
Aitken(1,Data, 1)
#extrapolN(1,Data,1)
extrapolyA(Data,1)





x=np.linspace(0,0.5,1000)  
plt.plot(x,x**2, color='black')
plt.gca().set_prop_cycle(None)      
for i in range(0,len(Masses)):
    for j in range(0,len(ls)):
        print(str(Masses[-i]), str(ls[j]))

        Data=np.loadtxt('ST_V2_zentrum_m'+str(Masses[-i])+'_l'+str(ls[j])+'.dat')
        A=extrapolyA(Data,0)
        
        #print(A)
        #STs[i][j],Errs[i][j]=extrapoly(Data, 0)
        STs[i][j]=A[0]
        Errs[i][j]=A[1]
        #print(A[0], A[1])
        #print(STs[i][j], Errs[i][j], "\n")
    plt.errorbar(ls, STs[i,:], Errs[i,:],linestyle='--', marker='.', markersize=10)
    #plt.show()


plt.gca().set_prop_cycle(None)
for i in range(0,len(Masses)):
    X_Y_Spline = make_interp_spline(ls,STs[i,:]) 
    #plt.plot(x,X_Y_Spline(x), linestyle='--')

plt.gca().set_prop_cycle(None)
for i in range(0,len(Masses)):
    plt.plot(-5,0.1, marker='.', linestyle='', markersize=8, label=str(Masses[i]))
#plt.plot(x,0*x, color='black')
plt.xlim(0,0.5)
plt.ylim(-0.05,0.25)

plt.legend(loc="upper left",handletextpad=-0.5, borderpad=0.4)

plt.xlabel('$l_0$',  fontsize=17)
plt.ylabel('$\\frac{2T}{g^2}$', fontsize=17, rotation=0)
plt.show()    
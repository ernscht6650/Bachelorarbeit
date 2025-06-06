import numpy as np
import matplotlib.pyplot as plt

ColN=3
ColY=2
ColObs=6

deg1=2
Fit1Range=list(range(3,8))
deg2=1
Fit2Range=list(range(0,9))

NumN=8
etas=list(range(100,151,5))
#etas=list(range(30,91,10))
ys=[]
Obs_infVol_y_s=[]
errs=[]
weights=[]
NumY=len(etas)

#Data=np.loadtxt('ST_Vol25_m'+m+'_l'+l+'.dat')
Data=np.loadtxt('testdata')

def extrapolN(y,Data, plot=0):
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
    return [p[deg1], np.sqrt(cov[deg1, deg1])]


def extrapoly(plot=0):
    Obs_infVol_y=[]*NumY
    errs=[]*NumY
    for eta in etas:
        y=eta/100
        ys.append(y)
        Obs_infVol_y,err=extrapolN(y,Data)
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
    return [p[deg2], np.sqrt(cov[deg2, deg2])]
#extrapolN(1,Data,1)
extrapoly(plot=1)
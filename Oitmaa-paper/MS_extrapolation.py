import ast
import numpy as np
import matplotlib.pyplot as plt


with open('MS_test.dat') as f:
    data = f.read()
dictVol = ast.literal_eval('{'+data+'}')

with open('MS_AllesMoegliche_N_y_l.dat') as f:
    data = f.read()
dict = ast.literal_eval('{'+data+'}')

def RenormierungVol(Vol, N, l0):
    return dictVol[str(Vol)+"_"+str(N)+"_"+str(l0)]

def Renormierung(N,y,l0):
	return dict[str(N)+"_"+str(y)+"_"+str(l0)]


def extrapolVol(Vol,N, Ls, plot=0):
    MSs=[]
    for l in Ls:
        MSs.append(N*RenormierungVol(Vol,N,l)/Vol)
    if plot==1:
        plt.plot(Ls,MSs, linestyle=' ', marker='.', markersize=10, label=str(N))
    return MSs

x=np.linspace(0,0.5,1000)


colors=['tab:blue','tab:orange','tab:green','tab:red','tab:purple','tab:brown','tab:pink','tab:gray','tab:olive','tab:cyan']

def extrapolVolume():
    Ls=np.array(range(25,476,25))/1000
    Ls2=np.array(range(25,476,25))/1000
    for N in range(10, 27,2):
        extrapolVol(25,N,Ls,1)
        MSs=extrapolVol(25,N, Ls2)
        p=np.polyfit(Ls2-0.25,np.array(MSs)-0.125,5)
        y=np.polyval(p,x-0.25)
        plt.plot(x,y+0.125)
        Lextrapol=[0.49] 
        for Le in Lextrapol:
            print("\""+str(25)+"_"+str(N)+"_"+str(Le)+"\":", (np.polyval(p,Le-0.25)+0.125)*25/N, ",")

    plt.legend(loc="lower left",handletextpad=-0.5, borderpad=0.4)
    plt.show()

def extrapolInfvol(N,y, Ls, plot=0, mogeln=0):
    MSs=[]
    for l in Ls:
        if l >= 0.25 and mogeln==1:
            MSs.append(0.25-Renormierung(N,y,round(0.5-l,4))/y)
        else:
            MSs.append(Renormierung(N,y,l)/y)
    if plot == 1:
       plt.plot(Ls, MSs, linestyle='', marker='.', markersize=10, label=str(N)+", "+str(y), color=colors[i])
    return MSs

def extrapolInvolFinal(N,y):
    Ls=[0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.2, 0.225, 0.25, 0.3, 0.35, 0.4, 0.45]#, 0.475, 0.485]
    Ls=[0.05, 0.1, 0.2, 0.3, 0.4]#, 0.475, 0.485]
    Ls2=np.array([ 0.125, 0.15, 0.175, 0.2, 0.225, 0.25, 0.275, 0.3, 0.325, 0.35, 0.375])
    Ls2=np.array([0.1, 0.2, 0.3, 0.4])
    extrapolInfvol(N,y,Ls,1,0)
    MSs=extrapolInfvol(N,y,Ls2,0,1)
    #plt.plot(Ls2,MSs )
    p=np.polyfit(Ls2-0.25,np.array(MSs)-0.125,3)
    #print(p)
    yfit=np.polyval(p,x-0.25)
    plt.plot(x,yfit+0.125, color=colors[i])
    
    #print(y*(np.polyval(p,-0.25)+0.125))
    print("\""+str(N)+"_"+str(y)+"_"+str(0)+"\":", (np.polyval(p,-0.25)+0.125)*y, ",")
    print("\""+str(N)+"_"+str(y)+"_"+str(0.5)+"\":", (np.polyval(p,0.25)+0.125)*y, ",")
#for N in range(10,25,4):
#    extrapolInvolFinal(N,1.0)
#plt.legend(loc="lower left",handletextpad=-0.5, borderpad=0.4)
#plt.show()
#extrapolVolume()


for eta in range(80, 95,5):
    y=eta/100
    i=0
    for N in range(24,25,2):
        extrapolInvolFinal(N,y)
        i=i+1


#extrapolVolume()
plt.legend(loc="upper left",handletextpad=-0.5, borderpad=0.4)
plt.show()
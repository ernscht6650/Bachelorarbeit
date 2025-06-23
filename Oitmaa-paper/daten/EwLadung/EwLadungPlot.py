import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True
plt.rcParams.update({'font.size': 15})


for N in [20, 16, 12, 8]:
    Data=np.loadtxt('EwLadung_N'+str(N)+'.dat')
    plt.plot(Data[:,0]-(N+1)/2, Data[:,3], linestyle='--', marker='',  markersize=10)

plt.xlabel("$n-\\frac{1}{2}(N+1)$")
plt.ylabel("$\\bar L(n)$")
#plt.ylim(0.084, 0.087)
plt.gca().set_prop_cycle(None)
for N in [20, 16, 12 , 8]:
    Data=np.loadtxt('EwLadung_N'+str(N)+'.dat')
    X_Y_Spline = make_interp_spline(Data[:,0]-(N+1)/2, Data[:,3])
    x=np.linspace(-N/2,N/2,1000)
    #plt.plot(x, X_Y_Spline(x), linestyle='--',  markersize=10) 
    plt.plot(Data[:,0]-(N+1)/2, Data[:,3], linestyle='', marker='.',  markersize=10, label=str(N))

plt.xticks([-10, -5, 0, 5, 10])
plt.legend(loc="upper left",handletextpad=-0.5, borderpad=0.4)
plt.show()
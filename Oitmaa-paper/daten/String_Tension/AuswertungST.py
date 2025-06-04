import numpy as np
import matplotlib.pyplot as plt




m='0'
l='0.3'
data = np.loadtxt('ST_m'+m+'_l_'+l+'.dat', comments="#", delimiter=" ", unpack=False)
#with open('ST_m'+m+'_l_'+l+'.dat') as f:
#    data = f.read()


NumN=8
NumY=7

deg1=3
F1R=[4, NumN-1]


Y=[]
P=[]
Bulklim=[]
#data=np.asmatrix(data)

for i in range(0,NumY):
    #print("\n",data[i*NumN+F1R[0]:i*NumN+F1R[1],3])
    #print(data[i*NumN+F1R[0]:i*NumN+F1R[1],6])
    P.append(np.polyfit(1/data[i*NumN+F1R[0]:i*NumN+F1R[1],3],data[i*NumN+F1R[0]:i*NumN+F1R[1],6],deg1))
    Y.append(data[i*NumN,2])
    Bulklim.append(P[i][deg1])

plt.plot(Y, Bulklim, '.')
plt.show()
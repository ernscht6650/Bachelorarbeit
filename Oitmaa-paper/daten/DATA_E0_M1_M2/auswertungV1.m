clc
clearvars
D=importdata("mg_Vol_y_M1_E0_M2_V1.dat")
NumVol=4
NumY=9
NumMasses=5

CurrMass=3
Obs=5
deg=6

D2=zeros(NumVol,NumY,NumMasses);
Y=zeros(NumVol,NumY);
indices=[1:1:NumY];

Colors=[[0 0 1]; [0 1 0]; [1 0 0]; [0 1 1]]

Vols=[10, 15, 20, 25];
N=[8:2:24];
x=linspace(0,3)
Fitpoints=[1:8]

for i=[1:NumVol]
    D2(i,indices,CurrMass)=D(((CurrMass-1)*NumY*NumVol+(i-1)*NumY)+indices,Obs);
    Y(i,:)=Vols(i)./N;
    
    p=polyfit(Y(i,Fitpoints),D2(i,Fitpoints,CurrMass), deg);
    plot(x, polyval(p,x), "-", "LineWidth", 2.5, "Color", Colors(i,:))
    hold on
    p(deg+1)
    plot(Y(i,:),D2(i,:,CurrMass), ".", "MarkerSize", 20, "Color", Colors(i,:))
end
hold off
ylim([-0.4 0])



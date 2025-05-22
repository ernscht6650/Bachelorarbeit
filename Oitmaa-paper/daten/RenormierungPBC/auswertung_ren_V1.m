clc
clearvars
D=importdata("RenNorm_mg_Vol_y_M1_W0_M2.dat")
NumVol=2
NumY=9
NumMasses=6

CurrMass=2
Obs=5
deg=2

Fitpoints=[3:9]

limits=zeros(6,2,3);
limits(:,:,1)=[[0.55 0.75]; [0.78 0.9]; [1.0 1.2]; [1.45 1.8]; [10 11]; [19.9 20.6]];
limits(:,:,2)=[[-0.33 -0.2]; [-0.33 -0.18]; [-0.33 -0.15]; [-0.33 -0.1]; [-0.33 -0.1]; [-0.33 -0.1]];
limits(:,:,3)=[[0.8 1.5]; [0.9 1.75]; [1.2 1.9]; [1.6 2.4]; [10 11]; [20 21]];

xlims=[[0 1.4]; [0 1]; [0 1.5]]

ylbl=["$M_V/g$", "$\omega_0/2Nx$", "$M_S/g$"]
Vol=["5" "10" "15" "20"]
Masses=["0" "0.125" "0.25" "0.5" "5" "10"]

D2=zeros(NumVol,NumY,NumMasses);
Y=zeros(NumVol,NumY);
indices=[1:1:NumY];

Colors=[[0 0 1]; [0 1 0]; [1 0 0]; [0.3  0.5 1]]

Vols=[10, 15, 20, 25];
N=[8:2:24];
x=linspace(0,2)

t=tiledlayout(3,2)

for CurrMass=[1:6]
    nexttile
    
    hold on
for i=[1:NumVol]
    D2(i,indices,CurrMass)=D(((CurrMass-1)*NumY*NumVol+(i-1)*NumY)+indices,Obs);
    Y(i,:)=Vols(i)./N;
    
    p=polyfit(Y(i,Fitpoints),D2(i,Fitpoints,CurrMass), deg);
    plot(x, polyval(p,x), "-", "LineWidth", 2, "Color", Colors(i,:))% "DisplayName", Vol(i))
    title( "$m/g=$"+Masses(CurrMass), "Interpreter","latex")
    hold on
    p(deg+1)
end
for i=[1:NumVol]

    plot(Y(i,:),D2(i,:,CurrMass), ".", "MarkerSize", 18, "Color", Colors(i,:))
end
if Obs==6
    legend("","", "20", "25", "interpreter", "latex","Location","northeast", "box", "on")
else
legend("","", "20", "25", "interpreter", "latex","Location","southeast", "box", "on")
end
box on
hold off
ylim(limits(CurrMass,:,Obs-3))
xlim(xlims(Obs-3,:))
xlabel("y", "Interpreter", "latex")
%ylabel(ylbl(Obs-3), "Interpreter","latex")

end

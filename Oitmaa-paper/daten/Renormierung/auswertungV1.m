clc
clearvars
D=importdata("Energien_Vol25.dat")
NumVol=1
NumY=9
NumMasses=4

CurrMass=1
Obs=7
deg=2

Fitpoints=[5:9]

limits=zeros(4,2,3);
limits(:,:,1)=[[0.45 0.65]; [0.79 1.15]; [1.03 1.35]; [1.5 1.85]];
limits(:,:,2)=[[-0.33 -0.15]; [-0.33 -0.18]; [-0.33 -0.15]; [-0.33 -0.1]];
limits(:,:,3)=[[0.7 1.5]; [1.35 1.7]; [1.5 1.9]; [1.95 2.4]];

xlims=[[0 1.4]; [0 1.4]; [0 1.5]]

ylbl=["$M_V/g$", "$\omega_0/2Nx$", "$M_S/g$", "$M_S/g$"]
Vol=["5" "10" "15" "20"]
Masses=["0" "0.125" "0.25" "0.5" "5" "10"]

D2=zeros(NumVol,NumY,NumMasses);
Y=zeros(NumVol,NumY);
indices=[1:1:NumY];

Colors=[[0 0 1]; [0 1 0]; [1 0 0]; [0.3  0.5 1]]

%Vols=[10, 15, 20, 25];
Vols=[25,25,20]
N=[10:2:26];
x=linspace(0,2)

t=tiledlayout(2,2)

for CurrMass=[1:1]
    nexttile
    
    hold on
for i=[1:NumVol]
    D2(i,indices,CurrMass)=D(((CurrMass-1)*NumY*NumVol+(i-1)*NumY)+indices,Obs);
    Y(i,:)=Vols(i)./N;
    
    p=polyfit(Y(i,Fitpoints),D2(i,Fitpoints,CurrMass), deg);
    plot(x, polyval(p,x), "-", "LineWidth", 2, "Color", Colors(i,:))% "DisplayName", Vol(i))
    %title( "$m/g=$"+Masses(CurrMass), "Interpreter","latex")
    hold on
    p(deg+1)
end
for i=[1:NumVol]

    plot(Y(i,:),D2(i,:,CurrMass), ".", "MarkerSize", 18, "Color", Colors(i,:))
end
if Obs==6
    legend("","","","","10", "15", "20", "25", "interpreter", "latex","Location","northeast", "box", "on")
else
legend("","","","","10", "15", "20", "25", "interpreter", "latex","Location","southeast", "box", "on")
end
box on
hold off
%ylim(limits(CurrMass,:,Obs-3))
%xlim(xlims(Obs-3,:))
xlabel("y", "Interpreter", "latex")
ylabel(ylbl(Obs-3), "Interpreter","latex")

end

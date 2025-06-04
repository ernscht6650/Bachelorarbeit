clc
clearvars

D1=importdata("Energien_Vol25.dat");
D2=importdata("EnergienVOl.dat")

ylbl=["$M_V/g$", "$\omega_0/2Nx$", "$M_S/g$", "$M_S/g$"]

obs=7
deg=2
x=linspace(0,2,1000)
FP1=[7:9]
FP2=[13:16]
FP3=[21:25]
FP4=[28:33]

 t = tiledlayout(3,1);
for obs=[5,4,7]
    nexttile
p1=polyfit(D1(FP1,3), D1(FP1,obs), deg)
p2=polyfit(D2(FP2,3), D2(FP2,obs), deg)
p3=polyfit(D2(FP3,3), D2(FP3,obs), deg)
p4=polyfit(D2(FP4,3), D2(FP4,obs), deg)


Colors=[[0 0 1]; [0 1 0]; [1 0 0]; [0.3  0.5 1]]

plot(D1(:,3), D1(:, obs), ".", MarkerSize=15, DisplayName="Ny=25, l=0.1", Color=Colors(1,:))
hold on

plot(D2([9:16],3), D2([9:16], obs), ".", MarkerSize=15, DisplayName="Ny=25, l=0.05", Color=Colors(2,:))
plot(D2([17:25],3), D2([17:25], obs), ".", MarkerSize=15, DisplayName="Ny=20, l=0.05", Color=Colors(3,:))
plot(D2([26:33],3), D2([26:33], obs), ".", MarkerSize=15, DisplayName="Ny=20, l=0.1", Color=Colors(4,:))

plot(x, polyval(p1,x), "-", "LineWidth", 2, 'HandleVisibility','off', Color=Colors(1,:))
plot(x, polyval(p2,x), "-", "LineWidth", 2, 'HandleVisibility','off', Color=Colors(2,:))
plot(x, polyval(p3,x), "-", "LineWidth", 2, 'HandleVisibility','off', Color=Colors(3,:))
plot(x, polyval(p4,x), "-", "LineWidth", 2, 'HandleVisibility','off', Color=Colors(4,:))


xlim([0,1.4])
xlabel("y", "Interpreter","latex")
ylabel(ylbl(obs-3), "Interpreter","latex")
hold off
if obs==5
    legend("location", "southeast")
end
end
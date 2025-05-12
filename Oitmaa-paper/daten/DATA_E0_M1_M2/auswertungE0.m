clc
clearvars
D=importdata("mg_y_N_M1_E0_M2_Alles.dat");

NumN=8;
NumY=24;
NumMasses=4;

CurMass=2;
Obs=6

deg=1;
deg2=4;

D2=zeros(NumN+1,NumY, NumMasses);
indices=[1:1:NumN];

for i=[1:NumY]
    D2(indices,i,CurMass)=D((CurMass-1)*(NumN*NumY)+indices+(i-1)*NumN,Obs);
end




for j=[1:NumY]
    p=polyfit(1./D(indices,3),D2(indices,j,CurMass),deg);
    D2(NumN+1,j,CurMass)=p(deg+1);
end
x=linspace(-0.1, 1.5, 1000);
xi=linspace(0, 0.101, 1000);

plot(xi, polyval(p,xi))
hold on
plot(1./D(indices,3),D2(indices,j,CurMass), ".")
hold off



p=polyfit(D([1:NumY]*NumN,2), D2(NumN+1,:,CurMass), deg2);
p(deg2+1)


A=zeros(1, NumY);

for i=1:NumY
    A(i)=D2(NumN+1, i,CurMass);
end

plot(D([1:NumY]*NumN,2), A, ".r", 'MarkerSize', 20)

hold on
plot(x, polyval(p,x), "-r", "LineWidth", 2.5)

B=zeros(NumN, NumY);

for i=1:NumY
    B(:,i)=D2(indices, i,CurMass);
end

for k=[1:NumN]
    plot(D([1:NumY]*NumN, 2), B(k,:) , ".k", 'MarkerSize', 15)
end

%a=[0];
%b=[-1/3.141592];
%plot(a, b, ".k", 'MarkerSize', 20)
hold off

xlim([0.0, 1.5])
ylim([0 2])

ax=gca;
ax.FontSize=30;
ax.LineWidth=2.5;
xlabel('$y$', 'Interpreter','latex')
ylabel('$\omega_0/2Nx$', 'Interpreter','latex')
%daspect([8 1 1])

%yticks([-0.3 -0.275 -0.25 -0.225 -0.2 -0.175 -0.15 -0.125 -0.1])
%yticklabels(["-0.3" "" "" "" "-0.2" "" "" "" "-0.1"])

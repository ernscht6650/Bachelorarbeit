clc
clearvars
D=importdata("GrundzustandV2_m0_y_N_E0.dat");

NumN=11;
NumY=10;
D2=zeros(NumN+1,NumY);
indices=[1:1:NumN];

for i=[1:NumY]
    D2(indices,i)=D(indices+(i-1)*NumN,3);
end

deg=6;
deg2=6;

for j=[1:NumY]
    p=polyfit(1./(2+2*indices),D2(indices,j),deg);
    D2(NumN+1,j)=p(deg+1);
end

p=polyfit(0.1*[1:10], D2(12,:), deg2)
x=linspace(-0.1, 1.1, 1000);

plot(0.1*[1:10], D2(NumN+1, :), ".r", 'MarkerSize', 20)

hold on
plot(x, polyval(p,x), "-r", "LineWidth", 2.5)

for k=[1:NumN]
    plot(0.1*[1:10], D2(k, :), ".k", 'MarkerSize', 15)
end

a=[0];
b=[-1/3.141592];
plot(a, b, ".k", 'MarkerSize', 20)
hold off

xlim([-0.01, 1.01])

ax=gca;
ax.FontSize=30;
ax.LineWidth=2.5;
xlabel('$y$', 'Interpreter','latex')
ylabel('$\omega_0/2Nx$', 'Interpreter','latex')
daspect([8 1 1])

yticks([-0.3 -0.275 -0.25 -0.225 -0.2 -0.175 -0.15 -0.125 -0.1])
yticklabels(["-0.3" "" "" "" "-0.2" "" "" "" "-0.1"])

clc
clearvars
D=importdata("mg0_y_N_M1.dat");

NumN=11;
NumY=8;
D2=zeros(NumN+1,NumY);
indices=[1:1:NumN];

for i=[1:NumY]
    D2(indices,i)=D(indices+(i-1)*NumN,3);
end

deg=5;
deg2=5;

for j=[1:NumY]
    p=polyfit(1./(2+2*indices),D2(indices,j),deg);
    D2(NumN+1,j)=p(deg+1);
end

p=polyfit(0.1*[3:2:17], D2(12,[1:NumY]), deg2)
x=linspace(-0.1, 2.1, 1000);

plot(0.1*[3:2:17], D2(NumN+1, :), ".r", 'MarkerSize', 20)

hold on
plot(x, polyval(p,x), "-r", "LineWidth", 2.5)

for k=[1:NumN]
    plot(0.1*[3:2:17], D2(k, :), ".k", 'MarkerSize', 15)
end

a=[0];
b=[1/sqrt(pi)];
plot(a, b, ".k", 'MarkerSize', 20)
hold off

xlim([-0.0, 1.8])
ylim([0.5 1.6])

ax=gca;
ax.FontSize=30;
ax.LineWidth=2.5;
xlabel('$y$', 'Interpreter','latex')
ylabel('$\frac{M_1}{g}$', 'Interpreter','latex')
%daspect([8 1 1])

%yticks([-0.3 -0.275 -0.25 -0.225 -0.2 -0.175 -0.15 -0.125 -0.1])
%yticklabels(["-0.3" "" "" "" "-0.2" "" "" "" "-0.1"])

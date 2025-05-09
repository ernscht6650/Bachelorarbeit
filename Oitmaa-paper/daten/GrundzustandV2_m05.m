clc
clearvars
D=importdata("mg05_y_N_M1_E0.dat");

NumN=11;
NumY=7;
D2=zeros(NumN+2,NumY);
indices=[1:1:NumN];

    
for i=[1:NumY]
    D2(indices+1,i)=D(indices+(i-1)*NumN,3);
    D2(1,i)=D(1+(i-1)*NumN,1);
end

deg=3;
deg2=4;

for j=[1:NumY]
    p=polyfit(1./(2+2*indices),D2(indices+1,j),deg);
    D2(NumN+2,j)=p(deg+1);
end

Bussje=[1:NumY]
p=polyfit(D2(1,Bussje), D2(NumN+2,Bussje), deg2)
x=linspace(-0.1, 2.1, 1000);

plot(D2(1,[1:NumY]), D2(NumN+2, :), ".r", 'MarkerSize', 20)

hold on
plot(x, polyval(p,x), "-r", "LineWidth", 2.5)

for k=[1:NumN]
    plot(D2(1,[1:NumY]), D2(k+1, :), ".k", 'MarkerSize', 15)
end

a=[0];
b=[1/sqrt(pi)];
plot(a, b, ".k", 'MarkerSize', 20)
hold off

xlim([-0.0, 1.8])
ylim([1 3])

ax=gca;
ax.FontSize=30;
ax.LineWidth=2.5;
xlabel('$y$', 'Interpreter','latex')
ylabel('$\frac{M_1}{g}$', 'Interpreter','latex')
%daspect([8 1 1])

%yticks([-0.3 -0.275 -0.25 -0.225 -0.2 -0.175 -0.15 -0.125 -0.1])
%yticklabels(["-0.3" "" "" "" "-0.2" "" "" "" "-0.1"])

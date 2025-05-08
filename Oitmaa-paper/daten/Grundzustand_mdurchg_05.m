clc
clearvars
I=importdata("mdurchg_0.5_Vol_y_Grundzustanddurch2xN.dat");

indices=[1:1:11];

n=7

p5 = polyfit(I(indices,2),I(indices,3),n)
p10 = polyfit(I(indices+11,2),I(indices+11,3),n)
p15 = polyfit(I(indices+22,2),I(indices+22,3),n)
p20 = polyfit(I(indices+33,2),I(indices+33,3),n)


x=linspace(-0.1,3.5,10000);

LW=3;
plot(x,polyval(p5,x), "-c", "LineWidth", LW)%, "DisplayName", "5")
hold on
plot(x,polyval(p10,x),"-b", "LineWidth", LW)%, "DisplayName", "10")
plot(x,polyval(p15,x),"-r", "LineWidth", LW)%, "DisplayName", "15")
plot(x,polyval(p20,x),"-m", "LineWidth", LW)%, "DisplayName", "20")

a=[0];
b=[-1/3.141592];
plot(a, b, ".k", 'MarkerSize', 20)


plot(I(indices+0*11,2), I(indices+0*11,3), ".c", "MarkerSize", 20, "DisplayName", "")
plot(I(indices+1*11,2), I(indices+1*11,3), ".b", "MarkerSize", 20)
plot(I(indices+2*11,2), I(indices+2*11,3), ".r", "MarkerSize", 20)
plot(I(indices+3*11,2), I(indices+3*11,3), ".m", "MarkerSize", 20)

hold off

xlabel('$y$', 'Interpreter','latex')
ylabel('$\frac{\omega_0}{2Nx}$', 'Interpreter','latex')
xlim([-0.0, 1.1])
ylim([-0.325 -0.1])

yticks([-0.3 -0.275 -0.25 -0.225 -0.2 -0.175 -0.15 -0.125 -0.1])
yticklabels(["-0.3" "" "" "" "-0.2" "" "" "" "-0.1"])

ax=gca;
ax.FontSize=30;
ax.LineWidth=2.5;

daspect([6 1 1]);

box on;
legend({"5", "10", "15", "20"}, "Location", "Southeast");
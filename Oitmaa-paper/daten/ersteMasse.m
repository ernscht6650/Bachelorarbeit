clc
clearvars
I=importdata("daten_Vol_y_E0_M1.dat");

indices=[1:1:10];

n=8

p5 = polyfit(I(indices,2),I(indices,4),n)
p10 = polyfit(I(indices+10,2),I(indices+10,4),n)
p15 = polyfit(I(indices+20,2),I(indices+20,4),n)
p20 = polyfit(I(indices+30,2),I(indices+30,4),n)


x=linspace(-0.1,3.5,10000);

LW=3;
plot(x,polyval(p5,x), "-c", "LineWidth", LW)%, "DisplayName", "5")
hold on
plot(x,polyval(p10,x),"-b", "LineWidth", LW)%, "DisplayName", "10")
plot(x,polyval(p15,x),"-r", "LineWidth", LW)%, "DisplayName", "15")
plot(x,polyval(p20,x),"-m", "LineWidth", LW)%, "DisplayName", "20")

a=[0];
b=[1/sqrt(pi)];
plot(a, b, ".k", 'MarkerSize', 20)


plot(I(indices+0*10,2), I(indices+0*10,4), ".c", "MarkerSize", 25, "DisplayName", "")
plot(I(indices+1*10,2), I(indices+1*10,4), ".b", "MarkerSize", 25)
plot(I(indices+2*10,2), I(indices+2*10,4), ".r", "MarkerSize", 25)
plot(I(indices+3*10,2), I(indices+3*10,4), ".m", "MarkerSize", 25)

hold off

xlabel('$y$', 'Interpreter','latex')
ylabel('$\frac{M_1}{g}$', 'Interpreter','latex')
xlim([-0.0, 2])
ylim([0.5 1])

%yticks([-0.3 -0.275 -0.25 -0.225 -0.2 -0.175 -0.15 -0.125 -0.1])
%yticklabels(["-0.3" "" "" "" "-0.2" "" "" "" "-0.1"])

ax=gca;
ax.FontSize=30;
ax.LineWidth=2.5;

daspect([3 1 1]);

box on;
legend({"5", "10", "15", "20"}, "Location", "Southeast");
clc
clearvars
I=importdata("daten_Vol_y_E0_M1.dat");

indices=[1:1:10];

n=5

p5 = polyfit(I(indices,2),I(indices,4),n)
p10 = polyfit(I(indices+10,2),I(indices+10,4),n)
p15 = polyfit(I(indices+20,2),I(indices+20,4),n)
p20 = polyfit(I(indices+30,2),I(indices+30,4),n)


x=linspace(0,3.5,1000);

hold on
for k=[0:1:3]
plot(I(indices+k*10,2), I(indices+k*10,4), ".")
end

plot(x,polyval(p5,x))
plot(x,polyval(p10,x))
plot(x,polyval(p15,x))
plot(x,polyval(p20,x))

hold off
%ylim([0.5,1.5])
%xlim([0, 3])
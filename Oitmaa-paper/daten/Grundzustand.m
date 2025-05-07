clc
clearvars
I=importdata("daten_Vol_y_E0_M1.dat");

indices=[1:1:11];

n=3

p5 = polyfit(I(indices,2),I(indices,3),n)
p10 = polyfit(I(indices+11,2),I(indices+11,3),n)
p15 = polyfit(I(indices+22,2),I(indices+22,3),n)
p20 = polyfit(I(indices+33,2),I(indices+33,3),n)


x=linspace(0,3.5,1000);

hold on
for k=[0:1:3]
plot(I(indices+k*11,2), I(indices+k*11,3), "+")
end

plot(x,polyval(p5,x))
plot(x,polyval(p10,x))
plot(x,polyval(p15,x))
plot(x,polyval(p20,x))

hold off

xlabel("y",)
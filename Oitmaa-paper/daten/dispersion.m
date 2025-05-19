clc
clearvars

D=importdata("Dispersion_N22_x3_mg0.dat")

A=[2:11]

plot(D(1,2), D(1,1), ".r", "MarkerSize", 30)
hold on
for i=[2:11]
    if D(i,3)<0
        plot(D(i,2), D(i,1), ".g", "MarkerSize", 30)
    else
        plot(D(i,2), D(i,1), ".b", "MarkerSize", 30)
    end
end

hold off

xlabel("$<O_P^2>$", "Interpreter","latex")
ylabel("$E$", "Interpreter","latex")

 dummyh2 = line(nan, nan, 'Linestyle', 'none', 'Marker', 'none', 'Color', 'none');
   legend(dummyh2, "$m/g=0$",  "Interpreter","latex", "Location","southeast", "Box","off")

ax=gca;
ax.FontSize=30;
ax.LineWidth=2.5;

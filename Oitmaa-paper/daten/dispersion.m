D=importdata("Dispersion_N22_x3.dat")

A=[1:11]
plot(D(A,2), D(A,1), ".k", "MarkerSize", 30)

xlabel("$<O_P^2>$", "Interpreter","latex")
ylabel("$E$", "Interpreter","latex")

ax=gca;
ax.FontSize=30;
ax.LineWidth=2.5;

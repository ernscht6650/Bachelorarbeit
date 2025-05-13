clc
clearvars
D=importdata("mg_y_N_M1_E0_M2_Alles.dat");

NumN=8;
NumY=24;
NumMasses=4;



CurMass=1;
Obs=4

deg=4;
deg2=5;
degMin=3
degMax=6

D2=zeros(NumN+1,NumY, NumMasses);
indices=[1:1:NumN];

for i=[1:NumY]
    D2(indices,i,CurMass)=D((CurMass-1)*(NumN*NumY)+indices+(i-1)*NumN,Obs);
end



x=linspace(-0.1, 1.5, 1000);
fitwerte=zeros(degMax,NumY);
Unsicherheiten=zeros(degMax,NumY);

for k=[degMin:degMax]
for j=[1:NumY]
    [p, delta]=polyfit(1./D(indices,3),D2(indices,j,CurMass),k);
    [y_fit,Uns] = polyval(p,0,delta);
    fitwerte(k,j)=y_fit(1);
    Unsicherheiten(k,j)=Uns(1);
end
end
D2(NumN+1,:,CurMass)=fitwerte(deg,:);
errors=zeros(2,NumY);

for j=[1:NumY]
    %fitwerte(:,j)-Unsicherheiten(:,j)
    errors(1,j)=D2(NumN+1,j,CurMass)-min(fitwerte([degMin:degMax],j)-Unsicherheiten([degMin:degMax],j));
    errors(2,j)=max(fitwerte([degMin:degMax],j)+Unsicherheiten([degMin:degMax],j))-D2(NumN+1,j,CurMass);
end


%for j=[1:NumY]
%    p=fit(1./D(indices,3),D2(indices,j,CurMass),'poly3','normalize','on')
%    p(0.1)
%%zend


xi=linspace(0, 0.101, 1000);

%plot(xi, polyval(p,xi))
%plot(xi, p(xi))
%hold on
%plot(1./D(indices,3),D2(indices,j,CurMass), ".")
%hold off



p=polyfit(D([1:NumY]*NumN,2), D2(NumN+1,:,CurMass), deg2);
p(deg2+1)


A=zeros(1, NumY);

for i=1:NumY
    A(i)=D2(NumN+1, i,CurMass);
end

%plot(D([1:NumY]*NumN,2), A, ".r", 'MarkerSize', 20)

plot(x, polyval(p,x), "-r", "LineWidth", 2.5)
hold on
errorbar(D([1:NumY]*NumN,2), A, errors(1,:), errors(2,:), ".k", 'MarkerSize', 20)



B=zeros(NumN, NumY);

for i=1:NumY
    B(:,i)=D2(indices, i,CurMass);
end

%for k=[1:NumN]
%    plot(D([1:NumY]*NumN, 2), B(k,:) , ".k", 'MarkerSize', 15)
%end

%a=[0];
%b=[-1/3.141592];
%plot(a, b, ".k", 'MarkerSize', 20)
hold off

xlim([0.0, 1.5])
%ylim([0.4 1.2])

ax=gca;
ax.FontSize=30;
ax.LineWidth=2.5;
xlabel('$y$', 'Interpreter','latex')
ylabel('$\omega_0/2Nx$', 'Interpreter','latex')
%daspect([8 1 1])

%yticks([-0.3 -0.275 -0.25 -0.225 -0.2 -0.175 -0.15 -0.125 -0.1])
%yticklabels(["-0.3" "" "" "" "-0.2" "" "" "" "-0.1"])

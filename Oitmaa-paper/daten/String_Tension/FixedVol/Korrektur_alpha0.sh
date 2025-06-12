for m in 0 0.05 0.1 0.2 0.3 0.35 0.4 0.8 1.6
do
	#for l in 0.005 0.05 0.1 0.2 0.3 0.4 0.45 0.475 0.485 0.495
	for l in 0.515 0.525 0.55 0.6 0.7 0.8 0.9 0.95
	do
		cat ./alteDaten_mit_falscher_Renormierung/ST_Vol25_m${m}_l${l}.dat ./Grundzustandsdichten/GZ_Dichte_m${m}_l0.dat | bash Filemerger.awk >> ST_Vol25_korr_m${m}_l${l}.dat
	done
done

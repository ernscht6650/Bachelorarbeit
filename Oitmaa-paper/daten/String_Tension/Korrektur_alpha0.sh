for m in 0 0.05 0.1 0.2 0.3 0.35 0.4 0.8 1.6
do
	for l in 0.05 0.1 0.2 0.3 0.4 0.45 0.475 0.485 0.49
	#for l in 0.515 0.525 0.55 0.6 0.7 0.8 0.9 0.95
	do
		bash Filemerger.awk alteDatenV2/STV2_m${m}_l${l}.dat GrundzustandsdichtenV2/GZ_DichteV2_sort_m${m}_l0.dat  ${m} > STV2_korr_m${m}_l${l}.dat
		echo $m $l
		cat STV2_korr_m${m}_l${l}.dat | wc -l
	done
done

for m in 0 0.05 0.1 0.2 0.3 0.35 0.4 0.8 1.6
do
	cat GZ_DichteV2_m${m}_l0.dat | sort -n > GZ_DichteV2_sort_m${m}_l0.dat
done


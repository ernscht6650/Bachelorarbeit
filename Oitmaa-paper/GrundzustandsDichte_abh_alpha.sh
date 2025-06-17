VOL=$1
Nmin=$2
Nmax=$3
delaym=$4

for l in 0.475 0.45 0.4 0.35 0.3 0.25 0.2 0.15 0.1 0.05
do
	for m in 0 0.05 0.1 0.2 0.3 
	do
		for N in $(seq ${Nmin} 2 ${Nmax})
		do
		python3 -c "from NonDecoOitmaa import*; print('\"'+str(${VOL})+'_'+str(${N})+'_'+str(${l})+'_'+str(${m})+'\": ', GrundzustandsenergieZentrumVol(${N},${VOL},${m},${l}), end=',\n')" >> Grundzustands_dictionary_Vol.dat &
		done
		sleep ${delaym}m
		sleep 20
	done
done





for l in 0.485 0.45 0.35 0.25  0.15 0.05
do
	for m in 0 0.05 0.1 0.2 0.3 
	do
		for N in $(seq ${Nmin} 2 ${Nmax})
		do
		python3 -c "from NonDecoOitmaa import*; print('\"'+str(${VOL})+'_'+str(${N})+'_'+str(${l})+'_'+str(${m})+'\": ', GrundzustandsenergieZentrumVol(${N},${VOL},${m},${l}), end=',\n')" >> Grundzustands_dictionary_Vol.dat &
		done
		sleep ${delaym}m
		sleep 20
	done
done

for l in 0.5 0.49 0.485 0.475 0.45 0.4 0.35 0.3 0.25 0.2 0.15 0.1 0.05
do
	for m in 0.35 0.4 0.8 1.6
	do
		for N in $(seq ${Nmin} 2 ${Nmax})
		do
		python3 -c "from NonDecoOitmaa import*; print('\"'+str(${VOL})+'_'+str(${N})+'_'+str(${l})+'_'+str(${m})+'\": ', GrundzustandsenergieZentrumVol(${N},${VOL},${m},${l}), end=',\n')" >> Grundzustands_dictionary_Vol.dat &
		done
		sleep ${delaym}m
	done
done


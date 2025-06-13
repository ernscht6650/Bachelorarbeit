VOL=$1
Nmin=$2
Nmax=$3
Delaym=$4



for m in 0.35
do
	for l in 0.15
	do
		for N in $(seq ${Nmin} 2 ${Nmax})
		do
		python3 -c "from NonDecoOitmaa import*; print('\"'+str(${VOL})+'_'+str(${N})+'_'+str(${l})+'_'+str(${m})+'\": ', GrundzustandsenergieZentrumVol(${N},${VOL},${m},${l}), end=',\n')" >> Grundzustands_dictionary_Vol.dat &
		done
		sleep 1m
	done
done

for m in 0.05
do
	for l in 0.03 0.4 0.45 0.475  0.49
	do
		for N in $(seq ${Nmin} 2 ${Nmax})
		do
		python3 -c "from NonDecoOitmaa import*; print('\"'+str(${VOL})+'_'+str(${N})+'_'+str(${l})+'_'+str(${m})+'\": ', GrundzustandsenergieZentrumVol(${N},${VOL},${m},${l}), end=',\n')" >> Grundzustands_dictionary_Vol.dat &
		done
		sleep ${Delaym}m
	done
done


for m in  0.1 0.2 0.3 0.35 0.4 0.8 1.6
do
	for l in 0 0.1 0.2 0.3 0.4 0.45 0.475  0.49
	do
		for N in $(seq ${Nmin} 2 ${Nmax})
		do
		python3 -c "from NonDecoOitmaa import*; print('\"'+str(${VOL})+'_'+str(${N})+'_'+str(${l})+'_'+str(${m})+'\": ', GrundzustandsenergieZentrumVol(${N},${VOL},${m},${l}), end=',\n')" >> Grundzustands_dictionary_Vol.dat &
		done
		sleep ${Delaym}m
	done
done

for m in 0 0.05 0.1 0.2 0.3 0.35 0.4 0.8 1.6
do
	for l in  0.05  0.15  0.25 0.35 0.485 0.5
	do
		for N in $(seq ${Nmin} 2 ${Nmax})
		do
		python3 -c "from NonDecoOitmaa import*; print('\"'+str(${VOL})+'_'+str(${N})+'_'+str(${l})+'_'+str(${m})+'\": ', GrundzustandsenergieZentrumVol(${N},${VOL},${m},${l}), end=',\n')" >> Grundzustands_dictionary_Vol.dat &
		done
		sleep ${Delaym}m
	done
done


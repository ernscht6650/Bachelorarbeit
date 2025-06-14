Nmin=$1
Nmax=$2
etamin=$3
etamax=$4
Delays=$5

for l in 0 0.5 
do
for m in 0 0.05 0.1 0.2 0.3 0.35 0.4 0.8 1.6
    do
    for eta in $(seq 95  5 ${etamax})
    do
    for N in $(seq ${Nmin} 2 ${Nmax})
    do	
	python3 -c "from NonDecoOitmaa import*; print('\"'+str(${N})+'_'+str(${eta}/100)+'_'+str(${l})+'_'+str(${m})+'\": ', GrundzustandsenergieZentrumV2(${N},${eta}/100,${m},${l}), end=',\n')" >> Grundzustands_dictionary_V2.dat &

    done
	echo $m $l ${eta}   
	sleep ${Delays}
	done
   done
done

for l in 0.5 
do
for m in 0 0.05 0.1 0.2 
    do
    for eta in $(seq 95  5 ${etamax})
    do
    for N in $(seq ${Nmin} 2 ${Nmax})
    do	
	python3 -c "from NonDecoOitmaa import*; print('\"'+str(${N})+'_'+str(${eta}/100)+'_'+str(${l})+'_'+str(${m})+'\": ', GrundzustandsenergieZentrumV2(${N},${eta}/100,${m},${l}), end=',\n')" >> Grundzustands_dictionary_V2.dat &

    done
	echo $m $l ${eta}   
	sleep ${Delays}
	done
   done
done



for l in 0.5
do
for m in 0.3 0.35 0.4 0.8 1.6
    do
    for eta in $(seq ${etamin} 5 ${etamax})
    do
    for N in $(seq ${Nmin} 2 ${Nmax})
    do	
	python3 -c "from NonDecoOitmaa import*; print('\"'+str(${N})+'_'+str(${eta}/100)+'_'+str(${l})+'_'+str(${m})+'\": ', GrundzustandsenergieZentrumV2(${N},${eta}/100,${m},${l}), end=',\n')" >> Grundzustands_dictionary_V2.dat &

    done
	echo $m $l ${eta}   
	sleep ${Delays}
	done
   done
done






for l in 0.45 0.4 0.35 0.3 0.25 0.2 0.15 0.1 0.05
do
for m in 0 0.05 0.1 0.2 0.3 0.35 0.4 0.8 1.6
    do
    for eta in $(seq ${etamin} 5 ${etamax})
    do
    for N in $(seq ${Nmin} 2 ${Nmax})
    do	
	python3 -c "from NonDecoOitmaa import*; print('\"'+str(${N})+'_'+str(${eta}/100)+'_'+str(${l})+'_'+str(${m})+'\": ', GrundzustandsenergieZentrumV2(${N},${eta}/100,${m},${l}), end=',\n')" >> Grundzustands_dictionary_V2.dat &

    done
	echo $m $l ${eta}   
	sleep ${Delays}
	done
   done
done


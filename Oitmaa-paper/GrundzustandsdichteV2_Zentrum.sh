Nmin=$1
Nmax=$2
etamin=$3
etamax=$4
Delays=$5

l=0.475
for eta in 85 90 95
do
for m in 0.35
do
    for N in $(seq ${Nmin} 2 ${Nmax})
    do	
	python3 -c "from NonDecoOitmaa import*; print('\"'+str(${N})+'_'+str(${eta}/100)+'_'+str(${l})+'_'+str(${m})+'\": ', GrundzustandsenergieZentrumV2(${N},${eta}/100,${m},${l}), end=',\n')" >> Grundzustands_dictionary_V2.dat &

    done
done
done

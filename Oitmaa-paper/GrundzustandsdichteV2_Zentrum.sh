Nmin=$1
Nmax=$2
etamin=$3
etamax=$4
Delays=$5

#sleep 30m

#for m in 0.4 
#do
#for l in 0.475
#    do
#    for eta in 120 125 130 135
#    do
#    for N in $(seq ${Nmin} 2 ${Nmax})
#    do
#	python3 -c "from NonDecoOitmaa import*; print('\"'+str(${N})+'_'+str(${eta}/100)+'_'+str(${l})+'_'+str(${m})+'\": ', GrundzustandsenergieZentrumV2(${N},${eta}/100,${m},${l}), end=',\n')" >> Grundzustands_dictionary_V2.dat &
        #python3 -c "from NonDecoOitmaa import *; print(${mdurchg}, 0,  ${eta}/100, ${N}, GrundzustandsenergieV2(${N}, ${eta}/100, ${mdurchg}))">> GZ_DichteV2_m${mdurchg}_l0.dat &
#    done
#   sleep ${Delays}s
#	done
#   done
#done


#for m in 0.4 
#do
#for l in 0.3 0.4 0.45 0.475
#    do
#    for eta in $(seq ${etamin} 5 ${etamax})
#    do
#    for N in $(seq ${Nmin} 2 ${Nmax})
#    do
#	python3 -c "from NonDecoOitmaa import*; print('\"'+str(${N})+'_'+str(${eta}/100)+'_'+str(${l})+'_'+str(${m})+'\": ', GrundzustandsenergieZentrumV2(${N},${eta}/100,${m},${l}), end=',\n')" >> Grundzustands_dictionary_V2.dat &
        #python3 -c "from NonDecoOitmaa import *; print(${mdurchg}, 0,  ${eta}/100, ${N}, GrundzustandsenergieV2(${N}, ${eta}/100, ${mdurchg}))">> GZ_DichteV2_m${mdurchg}_l0.dat &
#    done
#   sleep ${Delays}s
#	done
#   done
#done





for m in 1.6
do
for l in 0.4 0.45 0.475
    do
    for eta in $(seq ${etamin} 5 ${etamax})
    do
    for N in $(seq ${Nmin} 2 ${Nmax})
    do
	python3 -c "from NonDecoOitmaa import*; print('\"'+str(${N})+'_'+str(${eta}/100)+'_'+str(${l})+'_'+str(${m})+'\": ', GrundzustandsenergieZentrumV2(${N},${eta}/100,${m},${l}), end=',\n')" >> Grundzustands_dictionary_V2.dat &
        #python3 -c "from NonDecoOitmaa import *; print(${mdurchg}, 0,  ${eta}/100, ${N}, GrundzustandsenergieV2(${N}, ${eta}/100, ${mdurchg}))">> GZ_DichteV2_m${mdurchg}_l0.dat &
    done
   sleep ${Delays}
	done
   done
done

for mdurchg in 0 0.05 0.1 0.2 0.3 0.35 0.4 0.8 1.6
do
for l in 0.05 0.15 0.25 0.35 0.5
    do
	for eta in $(seq ${etamin} 5 ${etamax})
    do
    for N in $(seq ${Nmin} 2 ${Nmax})
    do
	python3 -c "from NonDecoOitmaa import*; print('\"'+str(${N})+'_'+str(${eta}/100)+'_'+str(${l})+'_'+str(${m})+'\": ', GrundzustandsenergieZentrumV2(${N},${eta}/100,${m},${l}), end=',\n')" >> Grundzustands_dictionary_V2.dat &
        #python3 -c "from NonDecoOitmaa import *; print(${mdurchg}, 0,  ${eta}/100, ${N}, GrundzustandsenergieV2(${N}, ${eta}/100, ${mdurchg}))">> GZ_DichteV2_m${mdurchg}_l0.dat &
    done
   sleep ${Delays}
   done
done
done

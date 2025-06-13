
l0=$1
Nmin=$2
Nmax=$3
etamin=$4
etamax=$5

for eta in $(seq ${etamin} 5 ${etamax})
    do
    for N in $(seq ${Nmin} 2 ${Nmax})
        do
            python3 -c "from NonDecoOitmaa import *; print('\"'+str(${N})+'_'+str(${eta}/100)+'_'+str(${l0})+'\": ', MassShift(${N}, ${eta}/100, ${l0}, -0.15*${eta}/100, 0.02), end=',\n')" >> MS_AllesMoegliche_N_y_l.dat &
        done
    done

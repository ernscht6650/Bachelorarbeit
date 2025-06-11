Vol=$1
Nmin=$2
Nmax=$3

for mdurchg in 0 0.05 0.1 0.2 0.3 0.35 0.4 0.8 1.6
do
    for N in $(seq ${Nmin} 2 ${Nmax})
    do
        python3 -c "from NonDecoOitmaa import *; print(${N},  ${mdurchg}, 0, ${Vol}, GrundzustandsenergieVol(${N}, ${Vol}, ${mdurchg}))">> GZ_Dichte_m${mdurchg}_l0.dat &
    done
done
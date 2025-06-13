Nmin=$1
Nmax=$2

for mdurchg in 0 0.05 0.1 0.2 0.3 0.35 0.4 0.8 1.6
do
    for eta in $(seq 100 5 150)
    do
    for N in $(seq ${Nmin} 2 ${Nmax})
    do
        python3 -c "from NonDecoOitmaa import *; print(${mdurchg}, 0,  ${eta}/100, ${N}, GrundzustandsenergieV2(${N}, ${eta}/100, ${mdurchg}))">> GZ_DichteV2_m${mdurchg}_l0.dat &
    done
   sleep 70s
   done
done

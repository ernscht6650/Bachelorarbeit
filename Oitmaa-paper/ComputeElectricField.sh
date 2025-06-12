
VOL=$1
Nmin=$2
Nmax=$3

for m in 0 0.05 0.1 0.2 0.3 0.35 0.4 0.8 1.6
do
    for l in 0 0.025 0.05 0.075 0.1 0.125 0.15 0.175 0.2 0.225 0.25 0.275 0.3 0.325 0.35 0.375 0.4 0.425 0.45 0.475 0.5
    do
        for N in $(seq ${Nmin} 2 ${Nmax})
        do
            python3 -c "from NonDecoOitmaa import *; mren=${m}-RenormierungVol(${VOL}, ${N}, ${l});  print(${N}, ${VOL}, ${l}, ${m}, Erwartungswert_Foverg(${N},${VOL}/${N},${l},mren))" >> EFeld_Vol${VOL}_m${m}_l${l}.dat &
        done
        sleep 15s 
    done
done


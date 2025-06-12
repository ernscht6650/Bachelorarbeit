VOL=$1
Nmin=$2
Nmax=$3

for m in 0 0.05 0.1 0.2 0.3 0.35 0.4 0.8 1.6
do
    for l in 0 0.05 0.1 0.2 0.3 0.4 0.45 0.475 0.525 0.55 0.6 0.7 0.8 0.9 0.95 
    do
        for N in $(seq ${Nmin} 2 ${Nmax})
        do
            python3 -c "from NonDecoOitmaa import *; mren=${m}-RenormierungVol(${VOL}, ${N}, ${l});  print(${N}, ${VOL}, ${l}, ${m}, Erwartungswert_Foverg(${N},${VOL}/${N},${l},mren))" >> ./daten/EFeld/EFeld_Vol${VOL}_m${m}_l${l}.dat &
        done
        sleep 7m 
    done
done


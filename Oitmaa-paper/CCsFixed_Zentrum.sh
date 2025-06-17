delay=$1

for m in 0 0.05 0.1 0.2 0.3 0.4 0.8 1.6
do
for l in  0 0.5 0.15 0.25 0.35
do
for N in $(seq 10 2 24)
do
python3 -c "from NonDecoOitmaa import *; CC=EW_Condensate_Zentrum(${m},${m}-RenormierungVol(25, ${N}, ${l}), ${l}, ${N}, 25/${N}); print(${N}, 25, ${m}, ${l}, CC[0], CC[1], CC[2], CC[3], CC[4])" >> CC_Vol25_m${m}_l${l}.dat &
done
echo $m $l
sleep ${delay}
done
done 

for m in 0 0.05 0.1 0.2 0.3 0.4 0.8 1.6
do
for l in 0.05 0.1 0.2 0.3 0.4 0.45 
do
for N in $(seq 10 2 24)
do
python3 -c "from NonDecoOitmaa import *; CC=EW_Condensate_Zentrum(${m},${m}-RenormierungVol(25, ${N}, ${l}), ${l}, ${N}, 25/${N}); print(${N}, 25, ${m}, ${l}, CC[0], CC[1], CC[2], CC[3], CC[4])" >> CC_Vol25_m${m}_l${l}.dat 
done
echo $m $l
sleep ${delay}
done
done 


for m in 0 0.05 0.1 0.2 0.3 0.4 0.8 1.6
do
for l in 0 0.05 0.1 0.15 0.2 0.25 0.3 0.35 0.4 0.45 0.5
do
mv CC_Vol25_m${m}_l${l}.dat CC_Vol25_zentrum_m${m}_l${l}.dat 
done
done

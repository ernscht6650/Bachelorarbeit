

for l in 0.15 0.25 0.35 0.65 0.75 0.85
do 
python3 -c "from OitmaaV2 import *; MassShiftVol(25,${l},26,10)" >> MS_Vol.dat &
sleep 20m
done


for m in  0 0.05 0.1 0.2 0.3 0.35 0.4 0.8 1.6
do
for l in 0.515 0.525 0.95 0.55 0.8 0.8 0.7 0.6 0.15 0.25 0.35 0.65 0.75 0.85
do
python3 -c "from OitmaaV2 import *; ComputeCondensate(25,${m}, ${l}, 10,26)" >> CC_Vol25_m${m}_l${l}.dat &
sleep 4m
done
done


for m in  0 0.05 0.1 0.2 0.3 0.35 0.4 0.8 1.6
do
for l in 0.15 0.25 0.35 0.65 0.75 0.85
do
python3 -c "from OitmaaV2 import *; ComputeStringtensionVol(25,${m}, ${l}, 10, 26)">> ST_Vol25_m${m}_l${l}.dat &
sleep 4m
done
done

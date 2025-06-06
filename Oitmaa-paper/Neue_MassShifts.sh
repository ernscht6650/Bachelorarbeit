

for l in 0.6 0.7 0.8 0.9 0.95 0.55 0.525 0.515
do 
python3 -c "from OitmaaV2 import *; MassShiftVol(25,${l},26,10)" >> MS_Vol.dat &
sleep 30m
done

for m in 0 0.05 0.1 0.2 0.3 0.35 0.4 0.8 1.6
do
for l in 0.05 0.1 0.2 0.3 0.4 0.45 0.475 0.485 0.49
python3 -c "from OitmaaV2 import *; ComputeCondensate(25,${m}, ${l}, 10,26)"
sleep 10m
done
done

for l in  0.6 0.7 0.8 0.9 0.95
do
python3 -c "from OitmaaV2 import *; ComputeMassShift(${l}, 24, 10, 85, 150)" >> MS_AllesMoegliche_N_y_l.dat &
sleep 80m
done

for l in 0.05 0.1 0.2 0.3 0.4 0.45 0.55
do
python3 -c "from OitmaaV2 import *; ComputeMassShift(${l},24,10, 85, 95)" >> MS_AllesMoegliche_N_y_l.dat &
sleep 15m
done

sleep 200m

for m in  0.3 0.35 0.4 0.8 1.6
do
for l in 0.6 0.7 0.8 0.9 0.95
do
python3 -c "from OitmaaV2 import *; ComputeStringtension(${m}, ${l}, 85, 150)" >> ./daten/String_Tension/STV2_m${m}_l${l}.dat &
sleep 35m
done
done


for m in  0 0.05 0.1 0.2 0.3 0.35 0.4 0.8 1.6
do
for l in 0.55
do
python3 -c "from OitmaaV2 import *; ComputeStringtension(${m}, ${l}, 85, 150)" >> ./daten/String_Tension/STV2_m${m}_l${l}.dat &
sleep 35m
done
done

for m in  0 0.05 0.1 0.2
do
for l in 0.6 0.7 0.8 0.9 0.95 
do
python3 -c "from OitmaaV2 import *; ComputeStringtension(${m}, ${l}, 85, 95)" >> ./daten/String_Tension/STV2_m${m}_l${l}.dat &
sleep 8m
done
done


for m in  0 0.05 0.1 0.2 0.3 0.35 0.4 0.8 1.6
do
for l in 0.05 0.1 0.2 0.3 0.4 0.45 
do
python3 -c "from OitmaaV2 import *; ComputeStringtension(${m}, ${l}, 85, 95)" >> ./daten/String_Tension/STV2_m${m}_l${l}.dat &
sleep 8m
done
done

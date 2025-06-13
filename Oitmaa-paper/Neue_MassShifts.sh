#sleep 120m
#for l in 0.175 0.075 0.125 
#do 
#bash MassShiftV2.sh ${l} 10 24 85 150
#python3 -c "from OitmaaV2 import *; ComputeMassShift(${l}, 24, 10, 85, 150)" >> MS_AllesMoegliche_N_y_l.dat &
#sleep 100m
#done

#for l in 0.05 
#do
#bash MassShiftV2.sh ${l} 10 24 85 95 
#python3 -c "from OitmaaV2 import *; ComputeMassShift(${l}, 24, 10, 80, 96):" >> MS_AllesMoegliche_N_y_l.dat &
#sleep 35m
#done
#sleep 30m




#for m in  0 0.05 0.1 0.2 0.3 0.35 0.4 0.8 1.6
#do
#for l in 0.515 0.525 0.95 0.55 0.8 0.8 0.7 0.6 0.15 0.25 0.35 0.65 0.75 0.85
#do
#python3 -c "from OitmaaV2 import *; ComputeCondensate(25,${m}, ${l}, 10,26)" >> CC_Vol25_m${m}_l${l}.dat &
#sleep 4m
#done
#done

for m in   0.3 
do
for l in 0.2 0.3 0.4 0.45
do
python3 -c "from OitmaaV2 import *; ComputeCondensateV2(${m}, ${l},10,24)" >> CC_V2_m${m}_l${l}.dat &
sleep 45m
done
done



for m in   0.3 0.35 0.4 0.8 1.6
do
for l in 0.05 0.1 0.2 0.3 0.4 0.45
do
python3 -c "from OitmaaV2 import *; ComputeCondensateV2(${m}, ${l},10,24)" >> CC_V2_m${m}_l${l}.dat &
sleep 45m
done
done


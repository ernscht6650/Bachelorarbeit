for m in  0.2 0.35 0.4 0.8 1.6
do
for l in 0.49 0.7 0.8 0.9 0.95
do
python3 -c "from OitmaaV2 import *; ComputeStringtension(${m}, ${l}, 100, 150)" >> ./daten/String_Tension/STV2_m${m}_l${l}.dat &
sleep 30m
done
done


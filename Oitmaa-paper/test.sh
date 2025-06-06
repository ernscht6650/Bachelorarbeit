for l in 0.3 0.4
do
for m in 0.1 0.2
do
echo $m, $l
python3 -c "from OitmaaV2 import *; ComputeStringtensionVol(25,${m},${l},10,10)" >> Test_m${m}_l${l}.dat &
done
sleep 3
done

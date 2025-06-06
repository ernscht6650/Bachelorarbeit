#sleep 5h

#cat MS_AllesMoegliche_N_y_l.dat >> dictionary2.txt
#cat brace  >> dictionary2.txt


#python3 -c "from OitmaaV2 import *; ComputeStringtension(0,0.05)" >> STV2_m0_l0.05.dat &



for m in  0.35 0.4 0.8 1.6
do
for l in 0.05 0.1 0.2 0.3 0.4 0.45 
do
python3 -c "from OitmaaV2 import *; ComputeStringtension(${m},${l})" >> STV2_m${m}_l${l}.dat &
sleep 22m
done

done

for m in 0.05 0.1 0.2 0.3 0.35 0.4 0.8 1.6
do
for l in 0.475 0.485, 0.49 
do
python3 -c "from OitmaaV2 import *; ComputeStringtension(${m},${l})" >> STV2_m${m}_l${l}.dat &
sleep 22m
done

done

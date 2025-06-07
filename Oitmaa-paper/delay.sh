#sleep 5h

#cat MS_AllesMoegliche_N_y_l.dat >> dictionary2.txt
#cat brace  >> dictionary2.txt


python3 -c "from OitmaaV2 import *; ComputeStringtension(0.8,0.49)" >> STV2_m0.8_l0.49.dat &

for m in  1.6
do
for l in 0.475 0.485, 0.49 
do
python3 -c "from OitmaaV2 import *; ComputeStringtension(${m},${l})" >> STV2_m${m}_l${l}.dat &
sleep 22m
done

done

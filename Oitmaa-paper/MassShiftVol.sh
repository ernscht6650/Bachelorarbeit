
VOL=$1
#L=$2
Nmin=$3
Nmax=$4

for L in 0.25 0.05 0.075 0.1 0.125 0.15 0.175 0.2 0.225 0.25 0.275 0.3 0.325 0.35 0.375 0.4 0.425 0.45 0.475
do

for N in $(seq ${Nmin} 2 ${Nmax})
do
python3 -c "from NonDecoOitmaa import *; print('\"'+str(${VOL})+'_'+str(${N})+'_'+str(${L})+'\": ', MassShift(${N}, ${VOL}/${N}, ${L}, -0.135*${VOL}/${N}, 0.02), end=',\n')" >> MS_test.dat&
done
sleep 300s
done

VOL=$1
#L=$2
Nmin=$3
Nmax=$4

for L in 0.525 
do

for N in $(seq ${Nmin} 2 ${Nmax})
do
python3 -c "from NonDecoOitmaa import *; print('\"'+str(${VOL})+'_'+str(${N})+'_'+str(${L})+'\": ', MassShift(${N}, ${VOL}/${N}, ${L}, -0.135*${VOL}/${N}, 0.02)*${N}/25, end=',\n')"&
done
sleep 5s
done

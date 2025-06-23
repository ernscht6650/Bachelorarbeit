delay=$1

PFAD=/home/users/fstein/Documents/Bachelorarbeit/Oitmaa-paper/daten/Massen

for l in 0 0.1 0.2 0.3 0.4 0.45 0.5
do
for m in 0 0.05 0.1 0.2 0.4 0.8 1.6
do
for  eta in $(seq 110 5 120)
do
for N in $(seq 10 2 24)
do
python3 << EOF  >> ${PFAD}/MassenV2_m${m}_l${l}.dat &
from NonDecoOitmaa import *
y=${eta}/100
N=${N}
l0=${l}
mdurchg=${m}

E=Skalar(mdurchg-Renormierung(N,y,l0),N,y, l0)

print(N,y,mdurchg,l0, E[0], E[1], E[2], E[3])

EOF
done
sleep ${delay}m
done
done
done

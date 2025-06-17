N=$1
eta=$2
m=$3
l=$4



PFAD=/home/users/fstein/Documents/Bachelorarbeit/Oitmaa-paper/daten/Massen


python3 << EOF  >> ${PFAD}/MassenV2_m${m}_l${l}.dat &
from NonDecoOitmaa import *
y=${eta}/100
N=${N}
l0=${l}
mdurchg=${m}

E=Skalar(mdurchg-Renormierung(N,y,l0),N,y, l0)

print(N,y,mdurchg,l0, E[0], E[1], E[2], E[3])

EOF


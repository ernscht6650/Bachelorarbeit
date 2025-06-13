#!/bin/bash

VOL=$1
Nmin=$2
Nmax=$3

PFAD=/home/users/fstein/Documents/Bachelorarbeit/Oitmaa-paper/daten/String_Tension/FixedVol/ZentrumsDichte

for  l in 0 0.1 0.2 0.3 0.4 0.45
do
for m in 0 0.05 0.1 0.2 0.35 0.4 0.8 1.6
do
python3 << EOF >> ${PFAD}/ST_Vol${VOL}_zentrum_m${m}_l${l}.dat
import ast
Vol=${VOL}
mdurchg=${m}
l0=${l}

with open('Grundzustands_dictionary_Vol.dat') as f:
    data = f.read()
dictVol = ast.literal_eval('{'+data+'}')

def GZDVol(Vol, N, mdurchg, l0):
        return dictVol[str(Vol)+"_"+str(N)+"_"+str(l0)+"_"+str(mdurchg)]

for N in range(${Nmin}, ${Nmax}+1,2):
	print(N, Vol, f"{mdurchg:3.2f}", f"{l0:3.2f}", f"{GZDVol(Vol, N, mdurchg, 0):15.13f}", f"{GZDVol(Vol, N, mdurchg, l0):15.13f}", f"{GZDVol(Vol, N, mdurchg, l0)-GZDVol(Vol, N, mdurchg, 0):15.13f}")
EOF
done
done

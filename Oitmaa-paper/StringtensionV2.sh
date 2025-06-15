#!/bin/bash

Nmin=$1
Nmax=$2

PFAD=/home/users/fstein/Documents/Bachelorarbeit/Oitmaa-paper/daten/String_Tension/ZentrumsDichteV2

for  l in 0 0.05 0.1 0.15  0.2 0.25  0.3 0.35 0.4 0.45 0.475 0.5
#for l in 0 0.1 0.2 0.3 0.4 0.475
do
for m in 0 0.05 0.1 0.2 0.3 0.35 0.4 0.8 1.6
do
python3 << EOF > ${PFAD}/ST_V2_zentrum_m${m}_l${l}.dat
import ast

mdurchg=${m}
l0=${l}

with open('Grundzustands_dictionary_V2.dat') as f:
    data = f.read()
dictVol = ast.literal_eval('{'+data+'}')

def GZDV2(N,y, mdurchg, l0):
        return dictVol[str(N)+"_"+str(y)+"_"+str(l0)+"_"+str(mdurchg)]

for eta in range(80,136,5):
	y=eta/100
	for N in range(${Nmin}, ${Nmax}+1,2):
		print(N, y, f"{mdurchg:3.2f}", f"{l0:3.2f}", f"{GZDV2(N,y, mdurchg, 0):15.13f}", f"{GZDV2(N,y, mdurchg, l0):15.13f}", f"{GZDV2(N,y, mdurchg, l0)-GZDV2(N,y, mdurchg, 0):15.13f}")
EOF
done
done

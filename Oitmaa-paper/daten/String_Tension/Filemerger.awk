awk -v v=$3 ' BEGIN {j=1};\
FNR==NR && $1==v{for (i=1; i<=4; i++){A[j,i]=$i}; A[j,5]=$6/$4; j++}; NR>FNR {print A[FNR, 1], A[FNR, 2],A[FNR, 3], A[FNR, 4], $5, A[FNR, 5], A[FNR,5]-$5} ' $1 $2 
#m l N omegaalpha/N omega0 ST y


#GSenergie von alpha neq 0 ist net auf n normiert

awk ' BEGIN {AnzahlZeilen1=9;};\
NR<=AnzahlZeilen1 {for (i=1; i<=4; i++){A[NR,i]=$i}; A[NR,5]=$6};\
NR> AnzahlZeilen1 {print A[NR-AnzahlZeilen1, 1], A[NR-AnzahlZeilen1, 2], A[NR-AnzahlZeilen1, 3], A[NR-AnzahlZeilen1, 4], A[NR-AnzahlZeilen1, 5] $5} '


#GSenergie von alpha neq 0 ist net auf n normiert

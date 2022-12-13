#!/bin/bash

ord() {
    LC_CTYPE=C printf '%d' "'$1"
}


charValue() {
    c=$1
    cASCII=$(ord $1)

    if [[ $c =~ [a-z] ]]
    then
        echo $(($cASCII - 96))
    else
        echo $(($cASCII - 38))
    fi
}

echo "part 1"

awk '
{
    split(substr($0, 1, length / 2), left, "")
    split(substr($0, length / 2 + 1, length / 2), right, "")
    for (i = 1; i <= length / 2; i++) {
        for (j = 1; j <= length / 2; j++) {
            if (left[i] == right[j]) {
                c=left[i]
            }
        }
    }
    dict[c]+=1
}
END {
    for (i in dict) {
        for (j = 1; j <= dict[i]; j++) {
            printf "%s", i
        }
    }
}
' ../data/3.in |
while read -n1 c
do
    echo $(charValue $c)
done | awk '{s+=$1} END {print s}'

echo "part 2"

awk '
{   
    if (NR % 3 == 1) {
        split($0, A, "")
    }
    else if (NR % 3 == 2) {
        split($0, B, "")
    }
    else {
        split($0, C, "")
        for (i = 1; i <= length(A); i++) {
            for (j = 1; j <= length(B); j++) {
                for (k = 1; k <= length(C); k++) {
                    if (A[i] == B[j] && B[j] == C[k]) {
                        badge=A[i]
                    }
                }
            }
        }
        dict[badge] += 1
    }

}
END {
    for (i in dict) {
        for (j = 1; j <= dict[i]; j++) {
            printf "%s", i
        }
    }
}
' ../data/3.in |
while read -n1 c
do
    echo $(charValue $c)
done | awk '{s+=$1} END {print s}'

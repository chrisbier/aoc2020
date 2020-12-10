#!/bin/bash

# Change one thing and run until it works
for x in {0..600}
do
    # Replace nop
    awk -v p='nop' -v n="$x" ' $0~p { i++ } ((i%n)==0) { sub(/^jmp/, "nop") }{print}' day8input > day8input_temp
    #python3 day8p2.py
    #echo "Count $x"
    if ! python3 day8p2.py
    then
        echo "Didn't find IT!"
    else
        echo "Found IT!"
        exit
    fi

done
# Replace jmp

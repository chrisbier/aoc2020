#!/usr/bin/python3
# Day 1

day1input = 'day1input'

inputfile = open(day1input, 'r')

listofnumbers2 = listofnumbers = inputfile.read().splitlines()

for ln in listofnumbers:
    for ln2 in listofnumbers2:
        # print(ln2)
        # print(int(ln)+int(ln2))
        for ln3 in listofnumbers:
            if (int(ln) + int(ln2) + int(ln3)) == 2020:
                print(ln, ' + ', ln2, ' + ', ln3, ' = 2020')
                print(int(ln)*int(ln2)*int(ln3))

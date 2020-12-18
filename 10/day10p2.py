#!/usr/bin/python3
# Day 10
#import sys
#import re
#import pprint

#pp = pprint.PrettyPrinter(indent=4)

inputfile = open('day10input', 'r')

input_list = [ int(x) for x in inputfile.read().split('\n') ]

# Sort the list
input_list.sort()
input_list.insert(0, 0)
highest = input_list[len(input_list) - 1]
input_list.append(highest + 3)
print(input_list)

# list index
list_index = 1

# Counter for knowing if it's the first or not
counter = 0

# Counter for 1 step
one_step_counter = 0
# Counter for 2 steps
two_step_counter = 0
# Counter for 3 steps
thr_step_counter = 0

for list_index in range(len(input_list)):
    pn_diff = int(input_list[list_index]) - int(input_list[list_index - 1])
    if pn_diff == 1:
        one_step_counter = one_step_counter + 1
    if pn_diff == 2:
        two_step_counter = two_step_counter + 1
    if pn_diff == 3:
        thr_step_counter = thr_step_counter + 1
    #list_index = list_index + 1

print(one_step_counter, thr_step_counter, one_step_counter * thr_step_counter)
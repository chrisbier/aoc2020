#!/usr/bin/python3
# Day 9
import sys
import re
import pprint

pp = pprint.PrettyPrinter(indent=4)

inputfile = open('day9input', 'r')

command_input_list = inputfile.read().split('\n')
#comparision_dict = { k:v for (k,True) in command_input_list}

# Ignore first 5 (preable)
index = 25
# Find group is previous 25
find_group = 25

def test_number(number, number_stack):
    if not number_stack:
        return False

    for tn in number_stack:
        if [x for x in number_stack if int(number) - int(tn) == int(x)]:
            print(number, number_stack)
            return True
        else:
            number_stack_temp = number_stack
            number_stack_temp.pop(0)
            if test_number(number, number_stack_temp):
                return True
            #print(number, number_stack_temp)
            #sys.exit(1)
    return False

# First 5 lines are the preable
while command_input_list[index]:
    number = command_input_list[index]
    temp_stack = [ value for value in command_input_list[index - find_group:index]]
    if not test_number(number, temp_stack):
        print(number)
        sys.exit('Found IT!')
    index = index + 1

# find first number that is not the sum of two of the 25 numbers before
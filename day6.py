#!/usr/bin/python3
# Day 4
import sys
import re

inputfile = open('day6input', 'r')

customs = []
customs_count = 0
customs_temp = inputfile.read().split('\n\n')

line_count = 0
# For loop to find IDs
# Check that the fields exist
for lines in customs_temp:
    group_customs = {}
    line_count = line_count + 1
    #print(line_count)
    
    # Separate \n 
    #lines_new = lines.replace('\n','')
    lines_new = lines.split('\n')
    #import pdb; pdb.set_trace();
    count_in_group = 0
    for k in lines_new:
        count_in_group = count_in_group + 1
        for l in k:
            #print(k)
            if l != ' ':
                if l in group_customs.keys():
                    group_customs.update({l: group_customs[l] + 1})
                else:
                    group_customs.update({l: 1})
    
    #print(group_customs, len(group_customs))
    # dump into list
    customs.append(group_customs)
    #print(group_customs, count_in_group)
    for u in group_customs:
        #print(u, group_customs[u], count_in_group)
        if group_customs[u] == count_in_group:
            customs_count = customs_count + 1
            print(u, group_customs[u], count_in_group, 'customs count', customs_count)

print(customs_count)
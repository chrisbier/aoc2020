#!/usr/bin/python3
# Day 4
import sys

inputfile = open('day4input2_example', 'r')

valid_passports = 0
passports = []
passports_temp = inputfile.read().split('\n\n')

def validate(passport):
    passport_template = {
        'byr': False, 
        'iyr': False, 
        'eyr': False,
        'hgt': False,
        'ecl': False,
        'pid': False,
        'cid': False,
        }
    
    if not 'cid' in passport.keys():
        passport.update({'cid': 0})

    if len(passport) < 8:
        return 0

    return 1
        

line_count = 0
# For loop to find IDs
# Check that the fields exist
for lines in passports_temp:
    user_passport = {}
    line_count = line_count + 1
    #print(line_count)
    
    # Separate \n 
    lines_new = lines.replace('\n',' ')
    lines_split_1 = lines_new.split(' ')
    #import pdb; pdb.set_trace();
    for kv in lines_split_1:
        #print(kv)
        (key_temp, value_temp) = kv.split(':')

        user_passport.update({key_temp: value_temp})
    
    # dump into list
    passports.append(user_passport)

for passport in passports:
    valid_passports = valid_passports + validate(passport)

#print(passports)
print(valid_passports)
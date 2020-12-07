#!/usr/bin/python3
# Day 4
import sys
import re

inputfile = open('day4input', 'r')

valid_passports = 0
passports = []
passports_temp = inputfile.read().split('\n\n')

def validate_year(test_year, start, end):
    if start <= int(test_year) <= end:
        return True
    return False

def validate_height(height):
    if 'cm' in height:
        height_number = int(height.split('cm')[0])
        if 150 <= height_number <= 193:
            return True

    if 'in' in height:
        height_number = int(height.split('in')[0])
        if 59 <= height_number <= 76:
            return True
    return False

def validate_hair(hair):
    # regex
    hr = re.compile(r"#[a-z0-9]{6}")
    match = hr.fullmatch(hair)
    if match:
        return True
    return False

def validate_eye(eye):
    eye_list = [ el for el in [ 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] if eye == el ]
    if eye_list:
        return True
    return False

def validate_pid(pid):
    vpid = re.compile(r"[0-9]{9}")
    match = vpid.fullmatch(pid)
    if match:
        return True
    return False

def validate(passport):
    year_tests = {
        'byr': {'start': 1920, 'end': 2002},
        'iyr': {'start': 2010, 'end': 2020}, 
        'eyr': {'start': 2020, 'end': 2030}
        }

    if not 'cid' in passport.keys():
        passport.update({'cid': 0})

    # Old Validation
    if len(passport) < 8:
        return 0

    # Test year fields
    #print('year')
    for test_year_field in year_tests:
        if not validate_year(passport[test_year_field], year_tests[test_year_field]['start'], year_tests[test_year_field]['end']):
            return 0

    #print('height')
    if not validate_height(passport['hgt']):
        return 0

    #print('hair')
    if not validate_hair(passport['hcl']):
        return 0

    #print('eye')
    if not validate_eye(passport['ecl']):
        return 0

    #print('pid')
    if not validate_pid(passport['pid']):
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
    #print(passport)
    valid_passports = valid_passports + validate(passport)

#print(passports)
print(valid_passports)
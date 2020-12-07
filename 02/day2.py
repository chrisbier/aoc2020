#!/usr/bin/python3
# Day 2

import sys

inputfile = open('day2input', 'r')

listofpasswords = [ x.split(' ') for x in inputfile.read().splitlines() ]

good_pw_count = 0

def count_letter(letter, password):
    count = 0
    #print('letter:', letter)
    #print('password:', password)
    for l in password:
        if l == letter:
            count = count + 1
    #print('Count:', count)
    return count

def check_password(pw_range, letter, password):
    letter_count = count_letter(letter, password)
    (pw1, pw2) = pw_range.split('-')
    pw_range_1 = int(pw1)
    pw_range_2 = int(pw2)

    if (pw_range_2 > letter_count > pw_range_1) or (letter_count == pw_range_2 or letter_count == pw_range_1):
        print('letter:', letter, 'password:', password, 'Count:', letter_count, 'range begin:', pw_range_1, 'end:', pw_range_2, 'SUCCESS')
        return 1
    #print('0')
    return 0


for ln in listofpasswords:
    #print(ln[0], ln[1][:-1], ln[2])
    #print('=========')
    check_result = check_password(ln[0], ln[1][:-1], ln[2])
    good_pw_count = good_pw_count + check_result

print('Good PW Count: %s' % good_pw_count)
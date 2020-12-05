#!/usr/bin/python3
# Day 4

import math

inputfile = open('day5input', 'r')

fb_seat = 127
lr_seat = 7
seat_id_max = 0

def calc_half(encoded, lower_seat, upper_seat):
    half = (upper_seat - lower_seat) / 2
    #print(encoded, lower_seat, upper_seat, half)
    if encoded == 'F' or encoded == 'L':
        #print(encoded, lower_seat, upper_seat - math.floor(half), half)
        return lower_seat, upper_seat - math.floor(half)
    else:
        #print(encoded, math.ceil(half) + lower_seat, upper_seat, half)
        return math.ceil(half) + lower_seat, upper_seat
    return False

def calc_seat(seat_raw, seat_number):
    lower_seat = 0
    upper_seat = seat_number

    for code1 in seat_raw:
        (lower_seat, upper_seat) = calc_half(code1, lower_seat, upper_seat)
    return lower_seat

def calculate_seatid(fb_seat, lr_seat):
    return (fb_seat * 8) + lr_seat

for seat_code in inputfile:
    fb_seat_temp = fb_seat
    lr_seat_temp = lr_seat

    # First 7 are FB
    seat_raw = seat_code[0:7]
    seat_row = calc_seat(seat_raw, fb_seat_temp)

    # Last 3 are LR
    lr_raw = seat_code[7:10]
    seat_side = calc_seat(lr_raw, lr_seat_temp)

    seat_id = calculate_seatid(seat_row, seat_side)
    if seat_id > seat_id_max:
        seat_id_max = seat_id
    #print(list(seat_code))
    #print('Row:', seat_row, 'Side:', seat_side, 'ID:', seat_id)
print(seat_id_max)
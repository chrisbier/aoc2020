#!/usr/bin/python3
# Day 11
#import sys
#import re
import pprint

pp = pprint.PrettyPrinter(indent=4)

inputfile = open('day11input_example', 'r')

input_list = inputfile.read().split('\n')

class SeatMatrix:

    seat_matrix = []
    new_seat_matrix = []
    has_changed_bool = False
    max_row = 0
    max_column = 0

    def __init__(self, initial_seat_matrix):
        self.seat_matrix = initial_seat_matrix.copy()
        self.new_seat_matrix = initial_seat_matrix.copy()
        self.max_row = len(self.seat_matrix) - 1
        self.max_column = len(self.seat_matrix[0]) - 1

    def dump(self):
        return self.new_seat_matrix

    def dumpold(self):
        return self.seat_matrix

    def get_has_changed(self):
        return self.get_has_changed

    def get_seat_value(self, column, row):
        if column < 0 or row < 0:
            return '.'
        if column > self.max_column - 1 or row > self.max_row - 1:
            return '.'
        
        return self.seat_matrix[row][column]

    def set_seat_value(self, column, row, seat_value):
        if column < 0 or row < 0:
            return '.'
        if column > self.max_column or row > self.max_row:
            return '.'

        new_row = self.new_seat_matrix[row][:column] + seat_value
        if column < self.max_column:
            end_values = self.new_seat_matrix[row][column + 1:]
            new_row = new_row + end_values
        self.new_seat_matrix[row] = new_row
        return new_row

    def surrounded(self, column, row):
        count = 0
        position_matrix = [
            (-1,-1), (0,-1), (1,-1),
            (-1,0), (1,0),
            (-1,1), (0,1), (1,1)
            ]

        for (p_column, p_row) in position_matrix:
            #print(self.get_seat_value(column + p_column, row + p_row))
            if self.get_seat_value(column + p_column, row + p_row) == '#':
                count = count + 1

        return count

    def empty_seat(self, column, row):
        self.set_seat_value(column, row, 'L')
        self.has_changed_bool = True

    def fill_seat(self, column, row):
        self.set_seat_value(column, row, '#')
        print(self.new_seat_matrix[row])
        self.has_changed_bool = True

seatmatrix = SeatMatrix(input_list.copy())

print("Start")
pp.pprint(input_list)

# Tests
#print(seatmatrix.get_seat_value(0, 1))
#print(seatmatrix.get_seat_value(1, 1))
#print(seatmatrix.get_seat_value(99, 96))
#print(seatmatrix.fill_seat(0,0))
#print(seatmatrix.fill_seat(1,0))
#print(seatmatrix.fill_seat(2,0))
#print(seatmatrix.fill_seat(0,1))
#print(seatmatrix.fill_seat(2,1))
##print(seatmatrix.fill_seat(0,2))
##print(seatmatrix.get_seat_value(1, 1))
##print(seatmatrix.empty_seat(1,1))
##print(seatmatrix.get_seat_value(1, 1))
#print(seatmatrix.surrounded(1,1))

# Loop through seats
#while not has_changed_bool:
for row in range(len(input_list)):
    for column in range(len(input_list[row])):
        surrounded_count = seatmatrix.surrounded(column, row)
        #print(column, row, surrounded_count)
        if surrounded_count > 3:
            seatmatrix.empty_seat(column, row)
        if surrounded_count == 0:
            seatmatrix.fill_seat(column, row)

print("End")
#pp.pprint(input_list)
#pp.pprint(seatmatrix.dumpold())
pp.pprint(seatmatrix.dump())
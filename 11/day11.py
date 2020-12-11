#!/usr/bin/python3
# Day 11
#import sys
#import re
import pprint

pp = pprint.PrettyPrinter(indent=4)

inputfile = open('day11input', 'r')

input_list = inputfile.read().split('\n')

has_changed_bool = True
old_seatmatrix = []

class SeatMatrix:

    seat_matrix = []
    new_seat_matrix = []
    has_changed_bool = False
    max_row = 0
    max_column = 0
    occupied_count = 0

    def __init__(self, initial_seat_matrix):
        self.import_matrix(initial_seat_matrix)
        self.max_row = len(self.seat_matrix)
        self.max_column = len(self.seat_matrix[0])

    def import_matrix(self, import_seat_matrix):
        self.seat_matrix = import_seat_matrix.copy()
        self.new_seat_matrix = import_seat_matrix.copy()

    def dump(self):
        return self.new_seat_matrix

    def dumpold(self):
        return self.seat_matrix

    def get_has_changed(self):
        return self.has_changed_bool

    def get_seat_value(self, column, row):
        if column < 0 or row < 0:
            return '.'
        if column > self.max_column - 1 or row > self.max_row - 1:
            return '.'
        
        return self.seat_matrix[row][column]

    def get_occupied_count(self):
        count = 0
        for row_out in self.new_seat_matrix:
            row_count = row_out.count('#')
            count = count + row_count
        return count

    def set_seat_value(self, column, row, seat_value):
        if column < 0 or row < 0:
            return '.'
        if column > self.max_column - 1 or row > self.max_row - 1:
            return '.'

        self.has_changed_bool = True

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

    def fill_seat(self, column, row):
        self.set_seat_value(column, row, '#')
        self.occupied_count = self.occupied_count + 1
        #print(self.new_seat_matrix[row])

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
while has_changed_bool:
    for row in range(len(input_list)):
        #print(row)
        for column in range(len(input_list[row])):
            #print("Column",column)
            is_a_seat = seatmatrix.get_seat_value(column, row)
            #print(column, row)
            if is_a_seat == 'L' or is_a_seat == '#':
                surrounded_count = seatmatrix.surrounded(column, row)
                #print(column, row, surrounded_count)
                if surrounded_count > 3:
                    seatmatrix.empty_seat(column, row)
                if surrounded_count == 0:
                    seatmatrix.fill_seat(column, row)
    has_changed_bool = seatmatrix.get_has_changed()
    print(has_changed_bool)
    if old_seatmatrix == seatmatrix.dump():
        print("Occupied", seatmatrix.get_occupied_count())
        break
    old_seatmatrix = seatmatrix.dump()
    seatmatrix = SeatMatrix(old_seatmatrix)
    #pp.pprint(seatmatrix.dump())


print("End")
#pp.pprint(input_list)
#pp.pprint(seatmatrix.dumpold())
pp.pprint(seatmatrix.dump())
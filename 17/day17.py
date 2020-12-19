#!/usr/bin/python3
# Day 17 part 1
import sys
#import re
import pprint

pp = pprint.PrettyPrinter(indent=4)

inputfile = open('day17input_example', 'r')

input_list = inputfile.read().split('\n')

# Try dict instead?  {'013': '#', '014': '#', '111': '#'}
class Cubes:
    cubes = [ [ [ '.' for x in range(10) ] for y in range(10) ] for z in range(10) ]
    cubes_new = []

    def __init__(self, initial_cube):
        dimension = 0
        row_index = 4
        for row in initial_cube:
            column_index = 4
            for column in row:
                self.cubes[dimension][row_index][column_index] = column
                column_index = column_index + 1
            row_index = row_index + 1
        self.cubes_new = self.cubes

    def dump(self):
        return {'X': self.cubes[0]}, {'Y': self.cubes[1]}, {'Z': self.cubes[2]}
    
    def get_cell(self, dimension, row, column):
        try:
            return self.cubes[dimension][row][column]
        except:
            return '.'
            #print(dimension, row, column)
            #sys.exit(1)

    def check_surrounding_cells(self, dimension, row, column):
        count = 0
        for dimension in range(0,1,2):
            for row in [ row - 2, row - 1, row + 1, row + 2]:
                for column in [ column - 2, column - 1, column + 1, column + 2]:
                    if '#' in self.get_cell(dimension, row, column):
                        print('count increment', dimension, row, column)
                        count = count + 1
        return count
    
    def process_matrix(self):
        for dimension in range(0,1,2):
            for row in range(0, len(self.cubes[dimension]) - 1):
                for column in range(0, len(self.cubes[dimension][row]) - 1):
                    cell = self.get_cell(dimension, row, column)
                    surround_count = self.check_surrounding_cells(dimension, row, column)
                    if '#' in cell:
                        print(cell, surround_count)
                        if 2 <= surround_count <= 3:
                            self.set_cell(dimension, row, column,'#')
                        else:
                            self.set_cell(dimension, row, column,'.')
                    if '.' in cell:
                        if surround_count == 3:
                            self.set_cell(dimension, row, column,'#')
        self.cubes = self.cubes_new 

        return True

    def set_cell(self, dimension, row, column, value):
        self.cubes_new[dimension][row][column] = value

cubes = Cubes(input_list)

pp.pprint(cubes.dump())

cubes.process_matrix()

pp.pprint(cubes.dump())

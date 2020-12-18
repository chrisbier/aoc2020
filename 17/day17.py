#!/usr/bin/python3
# Day 17 part 1
#import sys
#import re
import pprint

pp = pprint.PrettyPrinter(indent=4)

inputfile = open('day17input_example', 'r')

input_list = inputfile.read().split('\n')

class Cubes:
    cubes = [[[]]]

    def __init__(self, initial_cube):
        self.cubes = initial_cube

    def dump_cubes(self):


    def update_matrix(self):
        for dimension in [ 0, 1, 2]:
            for row in len(self.cubes[0]):


cubes = Cubes(input_list)


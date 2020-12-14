#!/usr/bin/python3
# Day 14
#import sys
#import re
import pprint

pp = pprint.PrettyPrinter(indent=4)

inputfile = open('day13input', 'r')

input_list = inputfile.read().split('\n')

class Memory:
    self.memory = []
    self.bitmask = ''

    def __init__(self):
        pass

    def update_mask(self, new_mask):
        self.bitmask = new_mask
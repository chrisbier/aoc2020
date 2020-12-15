#!/usr/bin/python3
# Day 14
#import sys
#import re
import pprint

pp = pprint.PrettyPrinter(indent=4)

inputfile = open('day14input_example2', 'r')

input_list = inputfile.read().split('\n')

class Memory:
    memory = [ 0 for iter in range(0, 99999) ]
    bitmask = ''

    def __init__(self):
        pass

    def update_mask(self, new_mask):
        self.bitmask = new_mask[::-1]
    
    def bit_not(self, n, numbits):
        return (1 << numbits) - 1 - n
    
    def process_mem_value(self, value):
        new_value = value
        for mask_bit_index in range(0, len(self.bitmask)):
            if self.bitmask[mask_bit_index] != 'X':
                mask_bit_value = 2 ** mask_bit_index
                bit_value = self.bitmask[mask_bit_index]
                bin_len_value = len(bin(value)) - 2
                bin_len_mask_bit_value = len(bin(mask_bit_value)) - 2

                if bit_value == '0':
                    if bin_len_value > bin_len_mask_bit_value:
                        new_value = self.bit_not(value | mask_bit_value, bin_len_value)
                    else:
                        new_value = self.bit_not(value | mask_bit_value, bin_len_mask_bit_value)
                    print('not', bin(self.bit_not(value, bin_len_value)),'|',bin(mask_bit_value),'=',bin(new_value), new_value, self.bitmask)
                else:
                    new_value = value | mask_bit_value
                    #print(bin(value),'|',bin(mask_bit_value),bin(value|mask_bit_value), value|mask_bit_value)
        return new_value
    
    def update_memory(self, location, value):

        new_value = self.process_mem_value(value)

        self.memory[location] = new_value

    def dump(self):
        return [ x for x in self.memory if x != 0 ]

mem = Memory()

for line in input_list:
    if 'mask' in line:
        # Update Mask
        mem.update_mask(line.split(' = ')[1])
    else:
        loc = int(line.split('[')[1].split('] ')[0])
        value = int(line.split(' = ')[1])
        mem.update_memory(loc, value)

mem_dump = mem.dump()
#pp.pprint(mem_dump)
print(sum(mem_dump))
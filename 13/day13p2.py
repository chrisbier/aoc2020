#!/usr/bin/python3
# Day 13 part 2
#import sys
#import re
import pprint
from functools import reduce

pp = pprint.PrettyPrinter(indent=4)

inputfile = open('day13input', 'r')

input_list = inputfile.read().split('\n')

class BusTimes:
    start_timestamp = 0
    bus_ids = []
    each_bus = []
    each_bus_marker = [True]
    max_iterations = 754999

    def __init__(self, start_time, bus_ids):
        self.start_timestamp = start_time
        self.bus_ids = bus_ids
        self.each_bus = [ bus for bus in bus_ids if bus != 'x' ]
    
    def calculate_bus_id(self, timestamp, bus_id):
        if timestamp % bus_id == 0:
            return True
        return False

    def is_bus_in_timestamp(self, timestamp, bus_id):
        temp_timestamp = timestamp + self.bus_ids.index(str(bus_id))
        print(timestamp, bus_id, temp_timestamp)
        result = self.calculate_bus_id(temp_timestamp, bus_id)
        if result:
            self.each_bus.append(bus_id)
            return True # temp_timestamp
        else:
            return False

    def run_through_buses(self, timestamp, bus_index):
        bus_id = self.each_bus[bus_index:][0]
        temp_timestamp = timestamp + self.bus_ids.index(bus_id)
        #print(temp_timestamp, bus_id)
        result = self.calculate_bus_id(temp_timestamp, int(bus_id))
        #print(result)
        if result:
            #print(temp_timestamp, bus_id)
            if self.each_bus[bus_index + 1:]:
                return self.run_through_buses(timestamp, bus_index + 1)
            else:
                #timestamp = temp_timestamp
                return result
        else:
            return False

    def run_new_calculations(self):
        timestamp = self.start_timestamp
        #while timestamp < self.max_iterations:
        while True:
            #print('Start:',timestamp, self.bus_ids[0])
            if self.run_through_buses(timestamp, 1):
                return timestamp
            timestamp = timestamp + int(self.bus_ids[0])
        return 0 # You don f'ed up A A Ron

    def chinese_remainder(self, n, a):
        sum = 0
        prod = reduce(lambda a, b: a*b, n)
        for n_i, a_i in zip(n, a):
            p = prod // n_i
            sum += a_i * self.mul_inv(p, n_i) * p
        return sum % prod
    
    def mul_inv(self, a, b):
        b0 = b
        x0, x1 = 0, 1
        if b == 1: return 1
        while a > 1:
            try:
                q = a // b
                a, b = b, a%b
                x0, x1 = x1 - q * x0, x0
            except ZeroDivisionError:
                print("Divide by ")
        if x1 < 0: x1 += b0
        return x1
 
# Split out data
starting_timestamp = int(input_list[0])
bus_data = input_list[1].split(',')

print(int(bus_data[0]), bus_data)

bus = BusTimes(int(bus_data[0]), bus_data)
print(bus.each_bus)

# Run calculations
#time_step = bus.run_new_calculations()
remainders = [ int(i) - int(bus.bus_ids.index(i)) for i in bus.bus_ids if i != 'x' ]
print(remainders)
time_step = bus.chinese_remainder( [ int(j) for j in bus.each_bus ], remainders)

#print('Bus ID', bus_data, 'Time Step', time_step) #, 'Output', bus_data * (time_step - starting_timestamp))
print(time_step)
#!/usr/bin/python3
# Day 13
#import sys
#import re
import pprint

pp = pprint.PrettyPrinter(indent=4)

inputfile = open('day13input', 'r')

input_list = inputfile.read().split('\n')

class BusTimes:
    start_timestamp = 0
    bus_ids = []
    max_iterations = 10

    def __init__(self, start_time, bus_ids):
        self.start_timestamp = start_time
        self.bus_ids = bus_ids
    
    def calculate_bus_id(self, timestamp, bus_id):
        if timestamp % bus_id == 0:
            return True
        return False

    def run_calculations(self):
        for time_step in range(self.start_timestamp, self.start_timestamp + self.max_iterations):
            for bus_id in self.bus_ids:
                result = self.calculate_bus_id(time_step, bus_id)
                if result:
                    return (bus_id, time_step)
        return (0, 0) # You don f'ed up A A Ron

# Split out data
starting_timestamp = int(input_list[0])
bus_data = input_list[1].split(',')

new_bus_ids = []
for bus_id in bus_data:
    if bus_id == 'x':
        pass
    else:
        new_bus_ids.append(int(bus_id))

print(starting_timestamp, new_bus_ids)

bus = BusTimes(starting_timestamp, new_bus_ids)

# Run calculations
(bus_id, time_step) = bus.run_calculations()

print('Bus ID', bus_id, 'Time Step', time_step, 'Output', bus_id * (time_step - starting_timestamp))
#!/usr/bin/python3
# Day 13 part 2
#import sys
#import re
import pprint

pp = pprint.PrettyPrinter(indent=4)

inputfile = open('day13input_example2', 'r')

input_list = inputfile.read().split('\n')

class BusTimes:
    start_timestamp = 0
    bus_ids = []
    each_bus = []
    each_bus_marker = [True]
    max_iterations = 10

    def __init__(self, start_time, bus_ids):
        self.start_timestamp = start_time
        self.bus_ids = bus_ids
        self.each_bus = [ bus for bus in bus_ids if bus != 'x' ]
    
    def calculate_bus_id(self, timestamp, bus_id):
        if timestamp % bus_id == 0:
            return True
        return False

    def is_bus_in_timestamp(self, timestamp, bus_id):
        temp_timestamp = timestamp + self.bus_ids.index(bus_id)
        result = self.calculate_bus_id(temp_timestamp, bus_id)
        if result:
            self.each_bus.append(bus_id)
            return temp_timestamp
        else:
            return 0


    def run_new_calculations(self):
        timestamp = self.start_timestamp
        while True:
            for bus_id in self.bus_ids[1:]:
                if bus_id != 'x':
                    result = self.is_bus_in_timestamp(timestamp, bus_id)
                    if result:
                        timestamp = temp_timestamp
                    #temp_timestamp = timestamp + self.bus_ids.index(bus_id)
                    #result = self.calculate_bus_id(temp_timestamp, bus_id)
                    #if result:
                    #    self.each_bus.append(bus_id)
                    #    timestamp = temp_timestamp
                    #else:
                    #    break
            if len(self.each_bus) == len(self.each_bus_marker)
            timestamp = timestamp + int(bus_id[0])
        return 0 # You don f'ed up A A Ron

# Split out data
starting_timestamp = int(input_list[0])
bus_data = input_list[1].split(',')

print(int(bus_data[0]), bus_data)

bus = BusTimes(int(bus_data[0]), bus_data)

# Run calculations
(bus_id, time_step) = bus.run_new_calculations()

print('Bus ID', bus_id, 'Time Step', time_step, 'Output', bus_id * (time_step - starting_timestamp))
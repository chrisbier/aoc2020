#!/usr/bin/python3
# Day 12
#import sys
#import re
import pprint

pp = pprint.PrettyPrinter(indent=4)

inputfile = open('day12input_example', 'r')

input_list = inputfile.read().split('\n')

class Navigation:
    
    #                  [E, N]
    current_location = [0, 0]
    # Starting direction
    current_facing_direction = 'E'
    direction_matrix = {
        'N': ( 0, 1),
        'E': ( 1, 0),
        'S': ( 0,-1),
        'W': (-1, 0)
    }
    order_of_directions = ['N', 'E', 'S', 'W']
    
    def __init__(self):
        pass

    def find_direction(self, direction):
        if direction in self.order_of_directions:
            self.current_facing_direction = direction
            return direction

        if direction == 'F':
            return self.current_facing_direction

        if direction == 'L':
            new_direction_index = self.order_of_directions.index(self.current_facing_direction)
            new_direction_index = new_direction_index - 1
            if new_direction_index == -1:
                new_direction_index = 3
        
        if direction == 'R':
            new_direction_index = self.order_of_directions.index(self.current_facing_direction)
            new_direction_index = new_direction_index + 1
            if new_direction_index > 3:
                new_direction_index = 0
        
        self.current_facing_direction = self.order_of_directions[new_direction_index]
        return self.current_facing_direction

    def calculate_distance(self, distance):
        (east_adj, north_adj) =  self.direction_matrix[self.current_facing_direction]
        (east_cur, north_cur) = self.current_location

        (east_new, north_new) = (0,0)

        if self.current_facing_direction == 'E' or self.current_facing_direction == 'W':
            east_new = east_cur + (distance * east_adj)

        if self.current_facing_direction == 'N' or self.current_facing_direction == 'S':
            north_new = north_cur + (distance * north_adj)

        print(east_new, north_new)
        new_coordinates = (east_new, north_new)
        return new_coordinates

    def process_direction(self, direction_encoding):
        direction = direction_encoding[0]
        distance = direction_encoding[1:]

        new_direction = self.find_direction(direction)
        print(new_direction, distance)

        self.current_location = self.calculate_distance(int(distance))

        return self.current_location


navigation = Navigation()

# Read in data
for direction in input_list:
    new_coordinates = navigation.process_direction(direction)
    print(new_coordinates)
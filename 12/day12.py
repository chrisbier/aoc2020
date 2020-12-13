#!/usr/bin/python3
# Day 12
#import sys
#import re
import pprint

pp = pprint.PrettyPrinter(indent=4)

inputfile = open('day12input', 'r')

input_list = inputfile.read().split('\n')

class Navigation:
    
    #                  [E, N]
    current_location = [0, 0]
    # Starting direction
    current_facing_direction = 'E'
    current_moving_direction = 'E'
    direction_matrix = {
        'N': ( 0, 1),
        'E': ( 1, 0),
        'S': ( 0,-1),
        'W': (-1, 0)
    }
    order_of_directions = ['N', 'E', 'S', 'W']
    
    def __init__(self):
        pass

    def find_direction(self, direction, distance):
        if direction in self.order_of_directions:
            #print(self.order_of_directions.index(direction))
            print('Facing: ', self.current_facing_direction)
            self.current_moving_direction = direction
            return direction

        if direction == 'F':
            self.current_moving_direction = self.current_facing_direction
            return self.current_facing_direction

        if direction == 'L':
            #print('Current Facing Direction',self.current_facing_direction)
            new_direction_index = self.order_of_directions.index(self.current_facing_direction)
            #print('new direction index', new_direction_index)
            if new_direction_index - int(distance / 90) < 0:
                new_direction_index = new_direction_index - int(distance / 90)
                new_direction_index = new_direction_index + 4
            else:
                new_direction_index = new_direction_index - int(distance / 90)
            #print('new direction index after', new_direction_index)
            if new_direction_index == -1:
                new_direction_index = 3
        
        if direction == 'R':
            print('Current Facing Direction',self.current_facing_direction)
            new_direction_index = self.order_of_directions.index(self.current_facing_direction)
            print('new direction index', new_direction_index)
            if new_direction_index + int(distance / 90) > 3:
                new_direction_index = new_direction_index + int(distance / 90)
                new_direction_index = new_direction_index - 4
            else:
                new_direction_index = new_direction_index + int(distance / 90)
            print('new direction index after', new_direction_index)
            if new_direction_index > 3:
                new_direction_index = 0
        
        print('Facing:', self.order_of_directions[new_direction_index])
        self.current_facing_direction = self.order_of_directions[new_direction_index]
        return self.current_facing_direction

    def calculate_distance(self, distance):
        (east_adj, north_adj) =  self.direction_matrix[self.current_moving_direction]
        (east_new, north_new) = (east_cur, north_cur) = self.current_location

        if self.current_moving_direction == 'E' or self.current_moving_direction == 'W':
            east_new = east_cur + (distance * east_adj)

        if self.current_moving_direction == 'N' or self.current_moving_direction == 'S':
            north_new = north_cur + (distance * north_adj)

        #print(east_new, north_new)
        new_coordinates = (east_new, north_new)
        return new_coordinates

    def process_direction(self, direction_encoding):
        direction = direction_encoding[0]
        distance = int(direction_encoding[1:])

        new_facing_direction = self.find_direction(direction, distance)
        print(new_facing_direction, distance)

        if direction == 'R' or direction == 'L':
            # Ignore distance
            pass
        else:
            self.current_location = self.calculate_distance(distance)

        return self.current_location


navigation = Navigation()
line = 0

# Read in data
for direction in input_list:
    line = line + 1
    print(line, '---------')
    print(direction)
    (en, nn) = new_coordinates = navigation.process_direction(direction)
    print(new_coordinates, '=', abs(en)+abs(nn))
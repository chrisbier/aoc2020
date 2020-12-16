#!/usr/bin/python3
# Day 15
#import sys
#import re
import pprint

pp = pprint.PrettyPrinter(indent=4)

inputfile = open('day15input', 'r')

input_list = inputfile.read().split(',')

class MemoryGame:

    number_list = ['X']

    def __init__(self):
        pass

    def add_number(self, number):
        self.number_list.append(number)
    
    def get_list(self):
        return self.number_list

    def find_prev_turns(self, number):
        list_size_max_index = len(self.number_list) - 1
        temp_list = self.number_list.copy()
        temp_list.reverse()
        #print(temp_list)
        last = (list_size_max_index - temp_list.index(number))
        #print('last', last)
        list_new = temp_list[:last + 1]
        #print('list new', list_new)
        #print(list_new.index(number))
        #prev = list_size_max_index - list_new.index(number)
        prev = list_new.index(number)
        #print('prev', prev)
        return (last, prev)

    def find_in_rev_list(self, mylist, number):
        for index in range(len(mylist) - 1, 0, -1):
            #print('mylist',mylist[index],'index', index)
            if mylist[index] == number:
                return index

    def find_prev_turns2(self, number):
        list_size_max_index = len(self.number_list) - 1
        temp_list = self.number_list.copy()
        list_new = temp_list[:-1]
        #print('list new', list_new, number)
        #print(list_new.index(number))
        #prev = list_size_max_index - (list_new.index(number) - 1)
        prev = self.find_in_rev_list(list_new, number)
        #print('prev', prev)
        return prev

    def count_number(self, number):
        return len([ cn for cn in self.number_list if cn == number ])

    def calculate_number(self, number_index):
        prev_number = self.number_list[number_index]
        #print(prev_number)
        count = self.count_number(prev_number)
        #print('count', count)
        if count <= 1:
            new_number = 0
        else:
            #(last_turn, prev_turn) = self.find_prev_turns(prev_number)
            last_turn = number_index
            prev_turn = self.find_prev_turns2(prev_number)
            #print('last turn', last_turn, 'prev turn', prev_turn)
            new_number = last_turn - prev_turn
        self.add_number(new_number)
        #print(self.number_list)
        return new_number

    def get_nth(self, nth_number):
        list_size = len(self.number_list)
        list_size_index = list_size - 1
        target_index = nth_number - 1

        if target_index > list_size_index:
            for index in range(list_size - 1, nth_number - 1):
                #print('index', index)
                self.calculate_number(index)

        return self.number_list[nth_number - 1]

game = MemoryGame()

for number in input_list:
    game.add_number(int(number))

print(game.get_nth(30000001))
print(game.get_list())
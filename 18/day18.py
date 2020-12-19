#!/usr/bin/python3
# Day 18 part 1
import sys
#import re
import pprint

pp = pprint.PrettyPrinter(indent=4)

inputfile = open('day18input_example2', 'r')

input_list = inputfile.read().split('\n')

# Try dict instead?  {'013': '#', '014': '#', '111': '#'}
class NewMath:

    def __init__(self):
        pass

    def easy_calc(self, list):
        if len(list) < 3:
            return False
        split_list = list.split(' ')
        (a, b, c) = split_list[0:3]
        total = eval(a+b+c)
        print(a,b,c,'=',total)

        if len(split_list) > 3:
            index_count = 3
            for item in split_list[3:]:
                if item.isdigit():
                    print('Total',str(total),'action:', str(split_list[index_count - 1]), 'number to add/mul', item)
                    total = eval(str(total) + str(split_list[index_count - 1]) + item)
                elif item == '+' or item == '*':
                    pass
                index_count = index_count + 1

        return total

    def process_list(self, count, list):
        total = 0
        if '(' in list:
            count = count + 1
            for chunk in list.split('('):
                total = total + self.process_list(chunk)
        elif ')' in list:
            total = total + self.easy_calc(list.replace(')'))
        else:
            total = self.easy_calc(list)
        return total

    def find_peren_close(self, plist):
        for item_index in range(len(plist)):
            if ')' in plist[item_index]:
                return item_index
            if '(' in plist[item_index]:
                return self.find_peren_close(plist[item_index + 1:])

    def process_list2(self, plist):
        total = 0
        if '(' in plist:
            for matching_peren in plist:
                if ')' in matching_peren:

            total_temp = self.process_list(plist[1:-1])

        elif ')' in plist:
            total = total + self.easy_calc(plist.replace(')'))
        else:
            total = self.easy_calc(plist)
        return total


newmath = NewMath()

total = 0
for line in input_list:
    new_line = line.replace('(', '( ').replace(')', ' )')
    total = total + newmath.process_list(new_line)
    print(line, '=', total)

print('Total:', total)
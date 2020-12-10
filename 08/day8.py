#!/usr/bin/python3
# Day 4
import sys
import re
import pprint

pp = pprint.PrettyPrinter(indent=4)

inputfile = open('day8input', 'r')

stack = []
stack_pointer = 0
accumulator = 0
loop_detector = {}

command_input_list = inputfile.read().split('\n')

def process_command(index, count, command, argument):
    print(index, count, command, argument)
    if command == 'acc':
        return index + 1, count + argument
    if command == 'jmp':
        return index + argument, count

    return index + 1, count

while stack_pointer > -1:
    if stack_pointer not in loop_detector:
        loop_detector.update({stack_pointer: True})
        print("Stack Pointer:",stack_pointer)
        # print(command_input_list[stack_pointer].split(' '))
        (cmd, cmd_arg) = command_input_list[stack_pointer].split(' ')
        #print(cmd, cmd_arg)
        (stack_pointer, accumulator) = process_command(stack_pointer, accumulator, cmd, int(cmd_arg))
    else:
        stack_pointer = -1
        print('Boot Loop detected')
        #print(loop_detector)
        #sys.exit('Boot Loop')
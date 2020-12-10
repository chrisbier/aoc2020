#!/usr/bin/python3
# Day 8
import sys
import re
import pprint

pp = pprint.PrettyPrinter(indent=4)

inputfile = open('day8input_temp', 'r')

stack = []
stack_pointer = 0
accumulator = 0
loop_detector = {}
last_good_stack_pointer = 0
last_good_accumulator = 0
already_boot_looped = 0

command_input_list = inputfile.read().split('\n')

def process_command(index, count, command, argument):
    #print(index, count, command, argument)
    if command == 'acc':
        return index + 1, count + argument
    if command == 'jmp':
        new_index = index + argument
        if new_index in loop_detector:
            #print(index, count, command, argument)
            #print("Ignore prev")
            #print(loop_detector)
            sys.exit(1)
            return index + 1, count
        return new_index, count
    #if command == 'nop':
        #print("NOP", argument)

    return index + 1, count

while stack_pointer > -1:
    #if stack_pointer not in loop_detector or already_boot_looped == 1:
    if True:
        loop_detector.update({stack_pointer: True})
        # print(command_input_list[stack_pointer].split(' '))
        try:
            (cmd, cmd_arg) = command_input_list[stack_pointer].split(' ')
        except:
            print("Command:", cmd, "Arg:", cmd_arg, "Stack Pointer:",stack_pointer, " Accumulator:", accumulator)
        #print("Command:", cmd, "Arg:", cmd_arg, "Stack Pointer:",stack_pointer, " Accumulator:", accumulator)
        #print("Command:", cmd, "Arg:", cmd_arg, "Stack Pointer:",stack_pointer, " Accumulator:", accumulator)
        #print(cmd, cmd_arg)
        last_good_stack_pointer = stack_pointer
        last_good_accumulator = accumulator
        (stack_pointer, accumulator) = process_command(stack_pointer, accumulator, cmd, int(cmd_arg))
    else:
        #stack_pointer = -1
        command_input_list[stack_pointer] = 'nop +0'
        (stack_pointer, accumulator) = process_command(last_good_stack_pointer, last_good_accumulator, cmd, int(cmd_arg))
        print('Boot Loop detected')
        already_boot_looped = 1
        print(loop_detector)
        sys.exit('Boot Loop')
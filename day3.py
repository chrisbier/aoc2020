#!/usr/bin/python3
# Day 3

inputfile = open('day3input', 'r')

pathwithtrees = inputfile.read().splitlines()

def replace_char(position, hillpath):
    before = position 
    after = position + 1
    if hillpath[position] == '#':
        return hillpath[:before] + 'X' + hillpath[after:]
    else:
        return hillpath[:before] + 'O' + hillpath[after:]

def check_tree(position, hillpath):
    hillpath_temp = hillpath
    if position > 31:
        position = position % 31

    #print(replace_char(position, hillpath_temp))

    if hillpath_temp[position] == '#':
        return 1
    return 0


# Right 1, down 1
scenario = [[1, 1]]
# Right 3, down 1
scenario.append([3, 1])
# Right 5, down 1
scenario.append([5, 1])
# Right 7, down 1
scenario.append([7, 1])
# Right 1, down 2
scenario.append([1, 2])

for x in scenario:
    slope = x[0]
    down = x[1]
    toboggan = 0
    tree_count = 0
    line_count = 1

    for line in pathwithtrees:
        if line_count % down == 0:
            tree_hit = check_tree(toboggan, line)
            toboggan = toboggan + slope
            tree_count = tree_count + tree_hit
        line_count = line_count + 1

    print(tree_count)
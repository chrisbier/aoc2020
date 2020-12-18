#!/usr/bin/python3
# Day 4
import sys
import re
import pprint

pp = pprint.PrettyPrinter(indent=4)

inputfile = open('day7input_example2', 'r')

rules_graph = lookup_graph = {'other': []}
bag_to_find = 'shiny gold'

rules_list = inputfile.read().replace('bags', 'bag').split('\n')

#get_numbers = re.compile('^[0-9]\s')

# Code by Eryk Kopczyński
#def find_shortest_path(graph, start, end):
#    dist = {start: [start]}
#    q = deque(start)
#    while len(q):
#        at = q.popleft()
#        for next in graph[at]:
#            if next not in dist:
#                dist[next] = [dist[at], next]
#                q.append(next)
#    return dist.get(end)

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath

line_count = 0
# For loop to find IDs
# Check that the fields exist
for lines in rules_list:
    line_count = line_count + 1
    rule_group = []
    rule_group_dict = {}
    #print(line_count)

    # Cleanup text
    new_line = lines.replace('.', '')
    new_line2 = new_line.replace(' no ', ' 0 ')

    # Separate root from contents
    parent_container = new_line2.split(' contain ')

    for children in parent_container[1].split(', '):
        #print(children)
        #print(child)
        #new_line = re.sub(get_numbers, lines)
        number_of_bags = children[0]
        #print(number_of_bags)

        tokenized_child = children.split(' ')
        #print(' '.join(tokenized_child[1:-1]))

        rule_group_dict.update({' '.join(tokenized_child[1:-1]): number_of_bags})
        rule_group.append(' '.join(tokenized_child[1:-1]))

    parent_container_actual = parent_container[0].split(' ')
    #print(' '.join(parent_container_actual[0:-1]))
    rules_graph.update({' '.join(parent_container_actual[0:-1]): rule_group})
    lookup_graph.update({' '.join(parent_container_actual[0:-1]): rule_group_dict})

#pp.pprint(rules_graph)
bag_count = 0
for start_bag in rules_graph:
    result_path = find_path(rules_graph, start_bag, bag_to_find)
    #print(result_path)
    if result_path:
        if len(result_path[0]) != 1:
            bag_count = bag_count + 1
print(bag_count)
#!/usr/bin/python3
# Day 4
import sys
import re
import pprint
import networkx as nx

pp = pprint.PrettyPrinter(indent=4)

inputfile = open('day7input_example2', 'r')

rules_graph = lookup_graph = {'other': []}
rules_graph2 = lookup_graph = {'other': []}
rules_graph_count = {'other': [0]}
bag_to_find = 'shiny gold'

rules_list = inputfile.read().replace('bags', 'bag').split('\n')

def count_and_find_all_path(graph, start, end, count_graph, counter=1, path=[]):
    path = path + [start]
    full_path = []
    if start == end:
        return [path], counter
    for node in graph[start]:
        #print(graph[start], node, count_graph[node])
        if count_graph[node] != 0:
            counter = counter * count_graph[node]
        if node not in path:
            (newpath, counter) = count_and_find_all_path(graph, node, end, count_graph, counter, path)
            for np in newpath:
                full_path.append(np)
    return full_path, counter

def find_all_path(graph, start, end, path=[]):
    path = path + [start]
    full_path = []
    if start == end:
        return [path]
    for node in graph[start]:
        if node not in path:
            newpath = find_all_path(graph, node, end, path)
        for np in newpath:
            full_path.append(np)
    return full_path

line_count = 0
# For loop to find IDs
# Check that the fields exist
for lines in rules_list:
    line_count = line_count + 1
    rule_group = []
    rule_group2 = []
    rule_group_dict = {}
    rule_group_count = []
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
        cc = int(number_of_bags)
        #print(number_of_bags)

        tokenized_child = children.split(' ')
        #print(' '.join(tokenized_child[1:-1]))
        #print(number_of_bags)
        key_name = ' '.join(tokenized_child[1:-1])
        rule_group_count.append(number_of_bags)
        rule_group_dict.update({key_name: number_of_bags})
        rule_group.append(key_name)
        while cc > 0:
            rule_group2.append(key_name)
            cc = cc - 1

    parent_container_actual = parent_container[0].split(' ')
    actual_name = ' '.join(parent_container_actual[0:-1])
    #print(' '.join(parent_container_actual[0:-1]), rule_group2)
    #print(rule_group)
    #print(rule_group_dict)
    rules_graph.update({actual_name: rule_group})

    print('before',rules_graph2)
    rules_graph2.update({actual_name: rule_group2})
    print('after', rules_graph2)
    print()
    
    lookup_graph.update({actual_name: rule_group_dict})
    
    rules_graph_count.update({actual_name: int(rule_group_count[0])})
    

#pp.pprint(rules_graph)

bag_count = 1
#for start_bag in rules_graph:
result_path1 = find_all_path(rules_graph, bag_to_find, 'other')
(result_path, counter) = count_and_find_all_path(rules_graph, bag_to_find, 'other', rules_graph_count)
#print(result_path)
#print(result_path, counter)
#print(rules_graph_count)

#print(rules_graph2)
count = 0
#for node in result_path1:
    

#if result_path:
#    result_path2 = result_path[0]
#    if len(result_path2) != 1:
#        print(result_path2)
#
#        temp_count = 1
#        for node in result_path2:
#            print(node,lookup_graph[node])
#            #temp_count = temp_count * int(lookup_graph[node])
#        bag_count = bag_count + temp_count

#print('Bags count for', bag_to_find, 'bag:', bag_count)
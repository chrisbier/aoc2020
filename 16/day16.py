#!/usr/bin/python3
# Day 16
#import sys
#import re
import pprint

pp = pprint.PrettyPrinter(indent=4)

inputfile = open('day16input', 'r')

input_list = inputfile.read().split('\n\n')

class Ticket:
    rules = {}
    ticket = []
    failures = []

    def __init__(self, rules):
        for rule in rules:
            (rule_name, rule_values) = rule.split(': ')
            (rule_range1, ignore_or, rule_range2) = rule_values.split(' ')
            (r1p1, r1p2) = rule_range1.split('-')
            (r2p1, r2p2) = rule_range2.split('-')
            self.rules.update({ rule_name: [ (int(r1p1), int(r1p2)), (int(r2p1), int(r2p2)) ] })

    def get_rules(self):
        return self.rules
    
    def get_failures(self):
        return self.failures
    
    def test_ticket(self, ticket):
        # If failes all tests
        failure = False

        for ticket_item_temp in [ x for x in ticket.split(',') ]:
            ticket_item = int(ticket_item_temp)
            fail_count = 0
            for rule in self.rules.values():
                ((range1p1, range1p2),(range2p1, range2p2)) = rule
                if range1p1 <= ticket_item <= range1p2 or range2p1 <= ticket_item <= range2p2:
                    # Do nothing
                    #print(range1p1 , ticket_item , range1p2 , range2p1 , ticket_item , range2p2)
                    pass
                else:
                    print(range1p1 , ticket_item , range1p2, ' or ' , range2p1 , ticket_item , range2p2)
                    fail_count = fail_count + 1
            if fail_count == len(self.rules):
                self.failures.append(ticket_item)
                failure = True

        return failure

rules = input_list[0].split('\n')
yourticket = input_list[1].split('\n')[1:]
nearby = input_list[2].split('\n')[1:]

nearby_tickets = Ticket(rules)

for ticket in nearby:
    nearby_tickets.test_ticket(ticket)

print(nearby_tickets.get_rules())
print(nearby_tickets.get_failures())
print(sum(nearby_tickets.get_failures()))

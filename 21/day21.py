#!/usr/bin/python3
# Day 21 part 1
import sys
#import re
import pprint
from collections import Counter

pp = pprint.PrettyPrinter(indent=4)

inputfile = open('day21input_example', 'r')

input_list = inputfile.read().split('\n')

# Try dict instead?  {'013': '#', '014': '#', '111': '#'}
class Ingredients:

    ingredient_list = []
    allergen_dict = {}
    results = {}
    results_least = []
    def __init__(self):
        pass

    def get_allergens(self):
        return self.allergen_dict

    def readline(self, line):
        (ingredients, allergen_temp) = (line[0], line[1])
        #print(ingredients,'|', allergen_temp[-1])
        allergen_list = allergen_temp[:-1].split(', ')
        ingredient_list = ingredients.split(' ')
        for ing in ingredient_list:
            self.ingredient_list.append(ing)

        #print('Allergens', allergen_list, 'Ingredients', ingredient_list)
        for allergen in allergen_list:
            if allergen in self.allergen_dict:
                new_list = self.allergen_dict[allergen]
                for x in ingredient_list:
                    # Exclude any not in both lists
                    if x in new_list:
                        new_list.append(x)
            else:
                new_list = ingredient_list
            self.allergen_dict.update({allergen: new_list})

    def most_likely(self):
        results_temp = {}
        for allergen in self.allergen_dict:
            results_least = Counter(self.allergen_dict[allergen])
            self.results_least.append(results_least)
            results = Counter(self.allergen_dict[allergen]).most_common(1)
            #counter = Counter(results)
            results_temp.update( { allergen: results } )
        self.results.update(results_temp)
        #self.results.update({key: value for key, value in sorted(results_temp.items(), key=lambda item: item[1])})
        return self.results
    
    def definitely_not2(self):
        # each result
        for x in self.results_least:
            print(list(x))
        # Only values of 1
        #return self.results_least
    
    def definitely_not(self):
        # each allergen
        definitely_not_allergen = self.ingredient_list
        for allergen in self.allergen_dict.values():
            #print('allergen',allergen)
            #print('def not allergen',definitely_not_allergen)
            definitely_not_allergen = list(set(definitely_not_allergen) | set(allergen))
        # Compare list and exclude items in other lists
        #print(definitely_not_allergen)
        return definitely_not_allergen

ingredients = Ingredients()

for line in input_list:
    ingredients.readline(line.split(' (contains '))

for (k,v) in ingredients.most_likely().items():
    print(k, v[0][0])# .keys()[-3:])

#defnot = ingredients.definitely_not()
#print(defnot, len(defnot))

defnot = ingredients.definitely_not2()
print(defnot, len(defnot))
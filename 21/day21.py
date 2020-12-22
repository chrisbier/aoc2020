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
    not_allergen_dict = {}
    results = {}
    results_least = []
    not_allergen_list = []

    def __init__(self):
        pass

    def get_allergens(self):
        return self.allergen_dict

    def readline(self, line):
        # Cleanup
        (ingredients, allergen_temp) = (line[0], line[1])
        allergen_list = allergen_temp[:-1].split(', ')
        ingredient_list = ingredients.split(' ')

        # Process ingredients into full list of everything
        self.ingredient_list = list(set(ingredient_list) | set(self.ingredient_list))

        # Process Allergens into allergen_dict
        if len(allergen_list) > 1:
            for allergen in allergen_list:
                if allergen in self.allergen_dict:
                    new_list = self.allergen_dict[allergen]
                    for x in ingredient_list:
                        # Exclude any in both lists
                        # Add if not in new_list
                        if x in new_list:
                            new_list.remove(x)
                        else:
                            new_list.append(x)
                else:
                    new_list = ingredient_list
                self.allergen_dict.update({allergen: new_list})
        else:
            allergen = allergen_list[0]
            if allergen in self.allergen_dict:
                new_list = self.allergen_dict[allergen]
                #new_list = list(set(new_list) | set(ingredient_list))
            else:
                new_list = ingredient_list
            self.allergen_dict.update({allergen: new_list})

    def play_it_again_sam(self, line):
        # Cleanup
        (ingredients, allergen_temp) = (line[0], line[1])
        allergen_list = allergen_temp[:-1].split(', ')
        ingredient_list = ingredients.split(' ')

        not_allergen = []

        for allergen in allergen_list:
            for ing in ingredient_list:
                if ing not in self.allergen_dict[allergen]:
                    not_allergen.append(ing)

        self.not_allergen_list.append(not_allergen)

    def most_likely(self):
        results_temp = {}
        for allergen in self.allergen_dict:
            results_least = Counter(self.allergen_dict[allergen])
            self.results_least.append(results_least)
            results = Counter(self.allergen_dict[allergen]).most_common(1)
            #counter = Counter(results)
            results_temp.update( { allergen: list(results) } )
        self.results.update(results_temp)
        #self.results.update({key: value for key, value in sorted(results_temp.items(), key=lambda item: item[1])})
        return self.results
    
    def definitely_not2(self):
        # for each ingredient, if not in any allergen list, then save to not list
        not_allergen_list = []

        for ing in self.ingredient_list:
            not_allergen_list.append(self.is_not_allergen(ing))
        not_allergen_list = [ x for x in not_allergen_list if x]
        return not_allergen_list
    
    def is_not_allergen(self, ing):
        non_allergen_temp = []
        for allergen in self.allergen_dict.values():
            #print(ing)
            if ing in allergen:
                return []
            else:
                non_allergen_temp.append(ing)
        return non_allergen_temp

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

for line in input_list:
    ingredients.play_it_again_sam(line.split(' (contains '))

#for (k,v) in ingredients.most_likely().items():
#    print(k, v[0][0])# .keys()[-3:])

print(ingredients.get_allergens())
print([x for x in ingredients.not_allergen_list if x])

#print(ingredients.ingredient_list)
#defnot = ingredients.definitely_not()
#print(defnot, len(defnot))

#defnot = ingredients.definitely_not2()
#print(defnot, len(defnot))
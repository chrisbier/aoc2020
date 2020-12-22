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
    allergen_list = []
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
        for ing in ingredient_list:
            self.ingredient_list.append(ing)

        # Process Allergens into allergen_dict
        for allergen in allergen_list:
            if allergen in self.allergen_dict:
                new_list = self.allergen_dict[allergen]
                new_list = list(set(new_list) & set(ingredient_list))
            else:
                new_list = ingredient_list
            self.allergen_dict.update({allergen: new_list})
    
    def definitely_not_3(self):
        self.allergen_list = [ item for allergen in self.allergen_dict.values() for item in allergen ]
        #print(self.allergen_list)
        print(self.ingredient_list)

        count = 0
        for ing in self.ingredient_list:
            if ing not in self.allergen_list:
                count = count + 1

        return count

    def cleanup_allergens(self, allergen):
        if len(self.allergen_dict[allergen]) > 1:
            # Get allergen list without this one
            for allergens in [ a for a in self.allergen_dict.keys() if a != allergen]:
                # for this list in the allergen_dict
                for ai in [x for x in self.allergen_dict[allergen] ]:
                    if ai in self.allergen_dict[allergens]:
                        self.allergen_dict[allergen].remove(ai)

ingredients = Ingredients()

for line in input_list:
    ingredients.readline(line.split(' (contains '))

#for line in input_list:
#    ingredients.play_it_again_sam(line.split(' (contains '))

#for (k,v) in ingredients.most_likely().items():
#    print(k, v[0][0])# .keys()[-3:])

print(ingredients.get_allergens())
print(ingredients.definitely_not_3())

for allergen in ingredients.allergen_dict.keys():
    ingredients.cleanup_allergens(allergen)

print(ingredients.get_allergens())
#print([x for x in ingredients.not_allergen_list if x])

#print(ingredients.ingredient_list)
#defnot = ingredients.definitely_not()
#print(defnot, len(defnot))

#defnot = ingredients.definitely_not2()
#print(defnot, len(defnot))
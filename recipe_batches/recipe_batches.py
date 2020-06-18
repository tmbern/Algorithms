#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
   # Divide the ingredient amounts by the recipe amount
   # if the amount is greater than or equal to 1 for all values, then you have enough.
   # if we round down to the nearest integer, then the total batches that we can make
   # will be the smallest integer in that array. 

    batch_arr = []
    for key, value in recipe.items():
        if key in ingredients:
            batch_arr.append(ingredients[key] // recipe[key])
        else:
            batch_arr.append(0)

    return min(batch_arr)
  
if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
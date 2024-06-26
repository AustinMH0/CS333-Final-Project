from recipemanager.ingredient import Ingredient
import collections


class Recipe:
    def __init__(self, name, prep_time, cook_time, servings):
        # self.ingredients = set()
        self.ingredients: set[Ingredient] = set()
        self.name = name
        self.prep_time = prep_time
        self.cook_time = cook_time
        self.servings = servings
        self.total_time = self.prep_time + self.cook_time
    
    def get_recipe_label(self, ingredient: Ingredient):
        return ingredient.label

    def get_ingredient_by_label(self, label):
        for ingredient in self.ingredients:
            if label in ingredient.label:
                return ingredient

    def add_multiple_ingredients(self, ingredients: set[Ingredient]):
        self.ingredients.update(ingredients)

    def add_ingredient(self, ingredient: Ingredient):
        self.ingredients.add(ingredient)

    def remove_ingredient(self, ingredient: Ingredient):
        self.ingredients.remove(ingredient)

    def remove_all_ingredients(self):
        self.ingredients.clear()

    def is_ingredient(self, label):
        for label in self.ingredients:
            if label in self.ingredients:
                return True

    def get_label_amount(self, label):
        for ingredients in self.ingredients:
            if label in ingredients.label:
                return ingredients.amount

    def get_amount_of_ingredient(self, amount):
        for ingredients in self.ingredients:
            if amount in ingredients.amount:
                return ingredients.label

    def ingredient_size(self):
        return len(self.ingredients)

    def get_total_time(self):
        return self.prep_time + self.cook_time

    def print_ingredients(self):
        for ingredient in self.ingredients:
            print(ingredient)
    
    def format_ingredients(self):
        ingredients = str(self.ingredients)[1:-1]
        # ingredients = ingredients.replace(', ', '\n')
        ingredients = ingredients.lstrip()
        return ingredients


    def __str__(self):
        ingredients = self.format_ingredients()
        return (f'Recipe: {self.name}\nPrep Time: {self.prep_time}\nCook Time: {self.cook_time}\nTotal Time: '
                f'{self.total_time} \nServings: '
                f'{self.servings}\n---Ingredients---\n{ingredients}\n')

    def __repr__(self):
        ingredients = self.format_ingredients()
        return (f'Recipe: {self.name}\nPrep Time: {self.prep_time}\nCook Time: {self.cook_time}\nTotal Time: '
                f'{self.total_time} \nServings: '
                f'{self.servings}\n---Ingredients---\n{ingredients}\n')

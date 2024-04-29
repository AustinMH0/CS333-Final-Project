from recipemanager.ingredient import Ingredient
import collections


class Recipe:
    def __init__(self, name, prep_time, cook_time, servings):
        self.ingredients = set()
        self.name = name
        self.prep_time = prep_time
        self.cook_time = cook_time
        self.servings = servings
        self.total_time = self.prep_time + self.cook_time

    def add_multiple_ingredients(self, ingredients: set[Ingredient]):
        # for ingredient in self.ingredients:
        #     self.ingredients.add(ingredients)
        self.ingredients.update(ingredients)

    def add_ingredient(self, ingredient: Ingredient):
        self.ingredients.add(ingredient)

    def remove_ingredient(self, ingredient: Ingredient):
        self.ingredients.discard(ingredient)

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

    def __str__(self):
        return (f'Recipe: {self.name}\nPrep Time: {self.prep_time}\nCook Time: {self.cook_time}\nTotal Time: '
                f'{self.total_time} \nServings: '
                f'{self.servings}\n {self.print_ingredients()}')

    def __repr__(self):
        return (f'Recipe: {self.name}\nPrep Time: {self.prep_time}\nCook Time: {self.cook_time}\nTotal Time: '
                f'{self.total_time} \nServings: '
                f'{self.servings}\n')

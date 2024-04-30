from recipemanager import *

def main():

    is_input = True
    while(is_input):
        print("------ Welcome to the Recipe Manager ------")
        recipe_name = input("Name of new recipe: ")
        recipe_prep = int(input("Recipe prep time: "))
        recipe_cook = int(input("Recipe cook time: "))
        recipe_serving = input("Recipe serving size: ")
        print('\n')

        my_recipe = Recipe(recipe_name, recipe_prep, recipe_cook, recipe_serving)
        print(my_recipe)

        ingredient_count = int(input("How many ingredients does this recipe have? "))
        for i in range(ingredient_count):
            ingredient_label = input("Ingredient label: ")
            ingredient_amount = input("Ingredient amount: ")
            my_ingredients = {Ingredient(ingredient_label, ingredient_amount)}
            my_recipe.add_multiple_ingredients(my_ingredients)
            
        print('\n')
        my_recipe.print_ingredients()

        user_continue = input("Continue? Y/N")
        if 'N' or 'n' in user_continue:
            is_input = False  

if __name__=="__main__": 
    main() 
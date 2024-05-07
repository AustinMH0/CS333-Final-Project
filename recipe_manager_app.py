from recipemanager import *
import os

def welcome_screen():
        print("------ Welcome to the Recipe Manager ------")
        print("(1) Add Recipe       (2) View Recipe Book")
        print("(3) Modify Recipe    (4) Remove Recipe")
        choice = input("Choose an option: ")
        return choice

def create_recipe():
        recipe_name = input("Name of new recipe: ")
        recipe_prep = int(input("Recipe prep time: "))
        recipe_cook = int(input("Recipe cook time: "))
        recipe_serving = input("Recipe serving size: ")
        print('\n')
        my_recipe = Recipe(recipe_name, recipe_prep, recipe_cook, recipe_serving)
        return my_recipe

def create_ingredients(recipe: Recipe):
        ingredient_count = int(input("How many ingredients does this recipe have? "))
        for _ in range(ingredient_count):
            ingredient_label = input("Ingredient label: ")
            ingredient_amount = input("Ingredient amount: ")
            ingredients = {Ingredient(ingredient_label, ingredient_amount)}
            recipe.add_multiple_ingredients(ingredients)

def remove_ingredients(recipe: Recipe):
    print("------Current Ingredients------")
    recipe.print_ingredients()
    choice = input("(1) Remove a single ingredient     (2) Remove all ingredients\n")
     
    if choice == '1':
        ingredient_input = input("Enter ingredient label: ")
        ingredient_to_remove = recipe.get_ingredient_by_label(ingredient_input)
        ingredient_label = recipe.get_recipe_label(ingredient_to_remove)
        print("Removing: " + ingredient_label)
        recipe.remove_ingredient(ingredient_to_remove)
    elif choice == '2':
        print("Removing all ingredients...")
        recipe.remove_all_ingredients()

def view_recipe_book(recipe_book: RecipeBook):
    recipe_book_size = str(recipe_book.get_recipe_book_size())
    print("------Recipe Book------")
    print("You have " + recipe_book_size + " recipes.")
    print("(1) View recipe book                 (2) View recipes by time")
    print("(3) View recipes by ingredients      (4) Sort recipes by time")
    choice = input("Choose an option: ")
    print('\n')

    if choice == "1":
         print("------Viewing Recipe Book------")
         print('\n')
         print(recipe_book)
    elif choice == "2":
         time_input = int(input("Enter a time value in minutes: "))
         recipes_by_time = recipe_book.get_recipes_by_time(time_input)
         print("------Viewing Recipes that are " + str(time_input) + " Minutes or Less------")
         recipes_by_time = format_list(recipes_by_time)
         print(recipes_by_time)
    elif choice == "3":
         ingredient_input = input("Enter an ingredient: ")
         recipes_by_ingredient = recipe_book.get_recipes_by_ingredients(ingredient_input)
         print("------Viewing Recipes that contain " + ingredient_input + "------")
         recipes_by_ingredient = format_list(recipes_by_ingredient)
         print(recipes_by_ingredient)
    elif choice == "4":
         print("------Sorting Recipes by Time------")
         sorted_recipes = recipe_book.sort_recipes_by_time()
         sorted_recipes = format_list(sorted_recipes)
         print(sorted_recipes)        
    

def modify_recipe(recipe_book: RecipeBook):
    input_recipe_name = input("Enter the name of the recipe you would like to modify: ")
    recipe_to_modify = recipe_book.get_recipe_by_name(input_recipe_name)
    recipe_name = recipe_book.get_name_of_recipe(recipe_to_modify)
    print("How would you like to modify " + recipe_name + "?")
    choice = input("(1) Add ingredient(s)      (2) Remove ingredient(s)\n")

    if choice == '1':
        create_ingredients(recipe_to_modify)
    elif choice == '2':
        remove_ingredients(recipe_to_modify)

def remove_recipe(recipe_book: RecipeBook):
    input_recipe_name = input("Enter the name of the recipe you would like to remove: ")
    recipe_to_remove = recipe_book.get_recipe_by_name(input_recipe_name)
    recipe_name = recipe_book.get_name_of_recipe(recipe_to_remove)
    print("Removing: " + recipe_name)
    recipe_book.remove_recipe(recipe_to_remove)

def format_list(list_to_format):
    formatted_list = str(list_to_format)[1:-1]
    formatted_list = formatted_list.replace(', ', '\n')
    return formatted_list


def main():
    os.system('clear')
    recipe_book = RecipeBook()

    # Comment for video
    # Comment for video
    # Comment for video 

    choice = ""

    while choice != 'quit':
        choice = welcome_screen()
        if choice == '1':
            my_recipe = create_recipe()
            create_ingredients(my_recipe)
            print("Adding " + my_recipe.name + " to Recipe Book \n")
            recipe_book.add_recipe(my_recipe)
        
        elif choice == '2':
            view_recipe_book(recipe_book)
        
        elif choice == '3':
            modify_recipe(recipe_book)
        
        elif choice == '4':
            remove_recipe(recipe_book)
        
        elif choice == 'quit':
            print(choice)
             
        print('\n')


if __name__=="__main__": 
    main() 
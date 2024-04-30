from recipemanager import *

def welcome_screen():
        print("------ Welcome to the Recipe Manager ------")
        print("(1) Add Recipe       (2) View Recipe Book")
        print("(3) Modify Recipe    (4) Remove Recipe")
        choice = input("Choose an option")
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
        for i in range(ingredient_count):
            ingredient_label = input("Ingredient label: ")
            ingredient_amount = input("Ingredient amount: ")
            ingredients = {Ingredient(ingredient_label, ingredient_amount)}
            recipe.add_multiple_ingredients(ingredients)

def remove_ingredients(recipe: Recipe):
    choice = input("(1) Remove a single ingredient     (2) Remove all ingredients")
     
    if choice == '1':
        ingredient_input = input("Enter ingredient label: ")
        ingredient_to_remove = recipe.get_ingredient_by_label(ingredient_input)
        print("Removing: " + ingredient_to_remove)
        recipe.remove_ingredient(ingredient_to_remove)
    elif choice == '2':
         print("Removing all ingredients...")
         recipe.remove_all_ingredients()

def view_recipe_book(recipe_book: RecipeBook):
    print("------Viewing Recipe Book------")
    print(recipe_book)

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


def main():

    recipe_book = RecipeBook()

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



        # user_continue = input("Continue? Y/N: ")
        # if user_continue == 'N' or 'n':
        #     is_input = False
        # elif user_continue == 'Y' or 'y':
        #     is_input = True  

if __name__=="__main__": 
    main() 
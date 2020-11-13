import sys
import os
from RecipeBook import RecipeBook
from Recipe import Recipe

path = None
recipeBook = RecipeBook()


# def _setdir(dest):
#     folder = os.path.abspath(dest)
#     print(folder)

def setpath():
    global path
    path = input("Where do you keep your recipes? ")
    path = os.path.abspath(path)
    print("Thank you.")
    print()


def loadrecipebook():
    global recipeBook
    recipe = Recipe.fromfile(path)
    recipeBook.addrecipe(recipe)


if __name__ == '__main__':
    # testRecipe = Recipe.fromfile("C:\\Users\\Corey\\Desktop\\SpiceRecipes\\test.txt")
    # recipeBook = RecipeBook()
    #
    # recipeBook.addrecipe(testRecipe)

    # print(testRecipe.name)
    # print(testRecipe.ingredients)
    # print(testRecipe.directions)

    # recipeBook.getrecipes()
    # recipeBook.getrecipe("Pasta")

    # _setdir("SpiceRecipesTest")

    setpath()
    loadrecipebook()

    # Gather Recipes in Path

    choice = None
    while choice != "exit":
        print("Current Path: " + path)
        print("[Menu]")
        print("[1] Change Recipe Folder")
        print("[2] Show all Recipes")
        print("[3] Search Recipe by name")
        print("Enter 'exit' to quit.")
        print("-" * 30)
        choice = input("Choice: ").lower().strip()

        if choice == str(1):
            setpath()
        elif choice == str(2):
            print()
            print("Recipes: ")
            recipeBook.getrecipes()
            print()
        elif choice == str(3):
            name = input("What is the name of the recipe? ").upper().strip()
            recipeBook.getrecipe(name)

    print("Goodbye!")
    sys.exit(0)

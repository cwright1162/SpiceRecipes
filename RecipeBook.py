import Recipe


class RecipeBook:
    def __init__(self, name="My Recipes"):
        # Initialize Recipe Book with Recipes
        self.name = name
        self.book = dict()

    def addrecipe(self, data: Recipe):
        name = data.name.upper()
        self.book[name] = data

    def getrecipes(self):
        try:
            for x in self.book:
                print(x)
        except:
            print("Recipe Book not found..")

    def getrecipe(self, name: str):
        key = name.upper()
        if key in self.book:
            print()
            print(name)
            print(self.book[key].ingredients)
            print(self.book[key].directions)
            print()
        else:
            print()
            print("No Recipe Found..")
            print()

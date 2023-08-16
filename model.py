from receipe import Recipe


class Model:
    """ Отвечает за внутреннюю логику работы программы.
    Здесь мы можем скрыть способы хранения данных, а также правила и алгоритмы обработки информации."""


    @staticmethod
    def get_recipe_from_db():
        recipes = Recipe.select().where(Recipe.cuisine == "Русская")
        return recipes

    @staticmethod
    def add_recipe_in_bd(recipe: tuple):
        title, author, description, ingredients, cuisine = recipe

        Recipe.create(title = title,
                      author = author,
                      description = description,
                      ingredients = ingredients,
                      cuisine = cuisine

                      )

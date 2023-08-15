from receipe import Recipe, db
import datetime
from model import Model
from controller import Controller



class View:
    """
    Отвечает за отображение данных Модели.
    На этом уровне мы лишь предоставляем интерфейс для взаимодействия пользователя с Моделью.

    """
    def __init__(self, model, controller):
        self.__model = model
        self.__controller = controller
        self.__controller.set_view(self)
        db.connect()

    @staticmethod
    def output_recipes(recipess):
        for item in recipess:
            print(item)

    def main(self):

        """ Сценарий 1. Вывести пользователю все статьи подряд """
        #self.__controller.get_films()
        """ Сценарий 2. Добавить новую статью """

        title = "Пельмени"
        author = "Русское народное"
        description = "Вкусные пельмени домашние"
        ingredients = "Тесто, мясо,перец, майонез"
        cuisine = "Русская"

        recipe = (title, author, description, ingredients, cuisine)
        self.__controller.add_recipe(recipe)


    def __del__(self):
        db.close()
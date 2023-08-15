from films import Films, db
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

        title = "Оно",
        director = "Крэзи До",
        year = "2020",
        description = "Очень страшное кино",
        actors = "Актеры очень много",
        duration = "2 часа"
        film = (title, director, year, description, actors, duration)
        self.__controller.add_film(film)


    def __del__(self):
        db.close()
from films import  Films
from datetime import date

class Model:
    """ Отвечает за внутреннюю логику работы программы.
    Здесь мы можем скрыть способы хранения данных, а также правила и алгоритмы обработки информации."""

    # @staticmethod
    # def create_tables():
    #     Films.create_table(['name', 'author', 'description', 'video', 'kitchen'])
    @staticmethod
    def get_films_from_db():
        films = Films.select().where(Films.year == "2023")
        return films

    @staticmethod
    def add_films(film: tuple):
        title, director, year, description, actors, duration = film
        Films.create(title = title,
                     director = director,
                     year = year,
                     description = description,
                     actors = actors,
                     duration = duration
                     )

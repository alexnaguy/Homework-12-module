from films import Films
from model import Model


class Controller:
    """
    Обеспечивает связь между Моделью и действиями пользователя в результате взаимодействия с Представлением.
    Принимает большинство решений о переходах приложения из одного состояния в другое.
    Также выполняет валидацию данных, если она проходит, то данные передаются в Model.
    """
    __view = None

    def __init__(self, model):
        self.__model = model

    def set_view(self, view):
        self.__view = view

    def get_films(self) -> None:
        # Запрос данных из Модели
        data = self.__model.get_films_from_db()
        # Отдать данные на представление
        self.__view.output_films(data)

    def add_film(self, film: tuple):
        # Запрос на добавление статьи
        self.__model.add_films(film)
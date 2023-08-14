from peewee import *

db = SqliteDatabase('films.db')


class Films(Model):

    class Meta:
        database = db

    title = CharField()
    director = CharField()
    year = CharField()
    description = TextField()
    actors = CharField()
    duration = CharField


    def __str__(self):
        return f"{self.title} \n" \
               f"{self.director} \n" \
               f"{self.year} \n" \
               f"{self.description}" \
               f"{self.actors}" \
               f"{self.duration}"

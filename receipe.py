from peewee import *

db = SqliteDatabase('recipe.db')


class Recipe(Model):

    class Meta:
        database = db
        db_table = "recipe"

    title = CharField()
    author = CharField()
    description = TextField()
    ingredients = TextField()
    cuisine = CharField()

def __str__(self):

        return f"{self.title} \n" \
               f"{self.author} \n" \
               f"{self.description}" \
               f"{self.ingridients}" \
               f"{self.cuisine} "
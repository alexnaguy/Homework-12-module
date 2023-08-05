import sqlite3
from sqlite3 import Error
from prettytable import from_db_cursor


def create_database(path: str) -> sqlite3.Connection:
    try:
        connection = sqlite3.connect(path)
    except Error as e:
        print(e)
    else:
        print(f'Соединение с базой данных {path} установлено.')
        return connection

# Создание таблицы
def create_table(cursor, sql_request, name_table: str):
    cursor.execute(sql_request)
    print(f'Таблица "{name_table}" создана.')

# Задание 2
#  Создайте базу данных «Продажи». База данных должна
#  содержать информацию о продавцах, покупателях, продажах. Необходимо хранить следующую информацию:
# продавцах: ФИО, email, контактный телефон;
# окупателях: ФИО, email, контактный телефон;
# о продажах: покупатель, продавец, название товара,
# цена продажи, дата сделки.

def execute_application():
    name_db = 'sales.db'
    connection = create_database(name_db)
    cursor = connection.cursor()
    #Создание таблиц
    name_table_sellers = 'sellers'
    sql_request_sellers = create_request_sellers_or_buyer(name_table_sellers)
    name_table_buyer = 'buyer'
    sql_request_buyer = create_request_sellers_or_buyer(name_table_buyer)
    name_table_sales = 'sales'
    sql_request_sales = create_request_sales(name_table_sales)
    try:
        create_table(cursor, sql_request_sellers, name_table_sellers)
        create_table(cursor, sql_request_buyer, name_table_buyer)
        create_table(cursor, sql_request_sales, name_table_sales)
    except Error as e:
        print(e)
    finally:
        cursor.close()
        connection.close()
        print(f'Соединение с базой данных {name_db} завершено.')


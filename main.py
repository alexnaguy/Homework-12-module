import sqlite3
import csv

# Задание 1.
# Создайте базу данных с одной таблицей People (имя, фамилия, страна,
# город, адрес, дата рождения).
# Добавьте возможность вставки, удаления и обновления данных через
# интерфейс приложения с помощью запросов INSERT, DELETE, UPDATE. Перед
# исполнением запроса проверяйте корректность названия таблицы.
# Добавьте к приложению возможность сохранять результаты работы
# фильтров в файл. Например, результат работы фильтра по отображению всех
# людей или результат работы фильтра по отображению людей из одного
# города.



# Создаем подключение к базе данных
connect = sqlite3.connect("peopleDB.db")

# Создать таблицу
cursor = connect.cursor()
table_name = "People"
def create_table(table_name):
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            country TEXT,
            city TEXT,
            address TEXT,
            birth_date TEXT
        )
    ''')
    print(f"Таблица {table_name} успешно создана")

# Добавить данные
def insert_person(first_name, last_name, country, city, address, birth_date):
    cursor.execute('''
        INSERT INTO People (first_name, last_name, country, city, address, birth_date)
        VALUES (?, ?, ?, ?, ?, ?)''', (first_name, last_name, country, city, address, birth_date))
    connect.commit()

# Функция для удаления данных
def delete_person(id_pers):
    cursor.execute('''
        DELETE FROM People WHERE id = ?
    ''', (id_pers))
    connect.commit()


# Функция для обновления данных
def update_person(old_value,  new_value):
    cursor.execute(f'''
        UPDATE People
        SET last_name = ? 
        WHERE last_name = ?
    ''', (new_value, old_value))
    connect.commit()


# Функция для сохранения результатов фильтрации в файл


def save_filtered(filename, filters):
    cursor.execute(f'SELECT * FROM People WHERE {filters}')
    results = cursor.fetchall()
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'First Name', 'Last Name', 'Country', 'City', 'Address', 'Birth Date'])
        writer.writerows(results)


def execute_application():
    # Создаем подключение к базе данных
    connect = sqlite3.connect("peopleDB.db")
    cursor = connect.cursor()
    # Создать таблицу
    table_name = "People"
    create_table(table_name)
    # Вставить данные
    insert_person('Дима', 'Иванов', 'Россия', 'Ярославль', 'Арбат 43', '1997-01-03')
    insert_person('Вася', 'Петров', 'Россия', 'Москва', 'Ямская 43', '1998-01-11')
    insert_person('Петр', 'Дегтярев', 'Россия', 'Москва', 'Комсомольская 87', '1994-05-06')

    # Удалить данные
    # delete_person("2")

    # Обновить данные
    # update_person("Иванов", "Пенько")

    # Запись данных с фильтрами
    filter = "city = 'Ярославль'"
    save_filtered('filtered_people.csv', filter)

    connect.close()


if __name__ == "__main__":
    execute_application()



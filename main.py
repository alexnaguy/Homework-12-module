import sqlite3

# Функция для создания базы данных и таблицы рекордов
def create_table():
    conn = sqlite3.connect('records.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Records (
            id INTEGER PRIMARY KEY,
            player_name TEXT,
            score INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Функция для добавления игрока
def add_record(player_name, score):
    conn = sqlite3.connect('records.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Records (player_name, score) VALUES (?, ?)", (player_name, score))
    conn.commit()
    conn.close()

# Функция для удаления  по ID
def delete_record(record_id):
    conn = sqlite3.connect('records.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Records WHERE id=?", (record_id,))
    conn.commit()
    conn.close()

# Функция для изменения по ID
def update_record(record_id, new_score):
    conn = sqlite3.connect('records.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE Records SET score=? WHERE id=?", (new_score, record_id))
    conn.commit()
    conn.close()

# Функция для полной очистки таблицы
def clear_table():
    conn = sqlite3.connect('records.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Records")
    conn.commit()
    conn.close()

# Функция для просмотра содержимого таблицы
def view_records():
    conn = sqlite3.connect('records.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Records ORDER BY score DESC")
    records = cursor.fetchall()
    conn.close()
    for record in records:
        print(record)

# Функция для отображения лучшей десятки
def view_top_ten():
    conn = sqlite3.connect('records.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Records ORDER BY score DESC LIMIT 10")
    top_records = cursor.fetchall()
    conn.close()
    for record in top_records:
        print(record)

# Создание базы данных и таблицы
create_table()

# Пример использования функций
add_record("Игрок 1", 100)
add_record("ИГрок 2", 150)
add_record("Игрок 3", 200)
add_record("Игрок 4", 250)
add_record("ИГрок 5", 260)
add_record("Игрок 6", 270)
add_record("Игрок 7", 275)
add_record("ИГрок 8", 280)
add_record("Игрок 9", 295)
add_record("Игрок 10", 300)
add_record("ИГрок 11", 320)
add_record("Игрок 12", 340)
update_record(2, 175)

delete_record(1)

view_records()

print("Top 10:")
view_top_ten()

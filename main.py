import sqlite3

# Функция для создания базы данных и таблицы заметок
def create_table():
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Notes (
            id INTEGER PRIMARY KEY,
            title TEXT,
            content TEXT,
            creation_date DATE,
            content_length INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Функция для добавления заметки пользователя в таблицу
def add_note(title, content):
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()
    content_length = len(content)
    cursor.execute("INSERT INTO Notes (title, content, creation_date, content_length) VALUES (?, ?, datetime('now'), ?)", (title, content, content_length))
    conn.commit()
    conn.close()

# Функция для удаления заметки из таблицы по ID
def delete_note(note_id):
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Notes WHERE id=?", (note_id,))
    conn.commit()
    conn.close()

# Функция для изменения заметки в таблице по ID
def update_note(note_id, new_title, new_content):
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()
    content_length = len(new_content)
    cursor.execute("UPDATE Notes SET title=?, content=?, content_length=? WHERE id=?", (new_title, new_content, content_length, note_id))
    conn.commit()
    conn.close()

# Функция для полной очистки таблицы
def clear_table():
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Notes")
    conn.commit()
    conn.close()

# Функция для просмотра содержимого таблицы
def view_notes():
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Notes ORDER BY creation_date DESC")
    notes = cursor.fetchall()
    conn.close()
    for note in notes:
        print(note)

# Функция для отображения первых десяти заметок
def view_first_ten():
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Notes ORDER BY creation_date DESC LIMIT 10")
    top_notes = cursor.fetchall()
    conn.close()
    for note in top_notes:
        print(note)



def execute_application():

    # Создание базы данных и таблицы
    create_table()

    # Пример использования функций
    add_note("Задача 1", "Приготовить завтрак.")
    add_note("Задача 2", "Заправить машину")
    add_note("Задача 3", "Поговорить с начальником.")
    add_note("Задача 4", "Cделать ...")
    add_note("Задача 5", "Cделать ...")
    add_note("Задача 6", "Cделать ...")
    add_note("Задача 7", "Cделать ...")
    add_note("Задача 8", "Cделать ...")
    add_note("Задача 9", "Cделать ...")
    add_note("Задача 10", "Cделать ДЗ ...")
    add_note("Задача 11", "Cделать ...")
    add_note("Задача 12", "Cделать ...")


    update_note(2, "Задача ", "Приехать на работу.")

    delete_note(1)

    view_notes()

    print("Первые десять заметок:")
    view_first_ten()

if __name__ == "__main__":
    execute_application()
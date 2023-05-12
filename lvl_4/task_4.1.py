# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)
# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.
# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:


import sqlite3

def db_connect():
    return sqlite3.connect("teatchers.db")

def db_close(connection):
    if connection:
        connection.close()


def create_db_table():
    try:
        connection = db_connect()
        cursor = connection.cursor()
        native_query = """create table Students (Student_Id Integer, Student_Name Text, School_Id Integer Primary key,
        constraint fk_school_id foreign key (School_Id) references School (School_Id));"""
        cursor.execute(native_query)
        connection.commit()
        print("Таблица создана успешно!")
        db_close(connection)
    except (Exception, sqlite3.Error) as error:
        print("Ошибка при выполнении запроса", error)

def data_for_db_table():
    try:
        connection = db_connect()
        cursor = connection.cursor()
        native_query = """insert into Students (Student_Id, Student_Name, School_Id) values (201, 'Иван', 1), 
        (202, 'Петр', 2), (203, 'Анастасия', 3), (204, 'Игорь', 4)"""
        cursor.execute(native_query)
        connection.commit()
        print("Данные внесены в таблицу успешно!")
        db_close(connection)
    except (Exception, sqlite3.Error) as error:
        print("Ошибка при выполнении запроса", error)


def inf_student(id):
    try:
        connection = db_connect()
        cursor = connection.cursor()
        native_query = """select Students.Student_Id, Students.Student_Name, Students.School_Id, School.School_Name 
        from Students join School on Students.School_Id = School.School_Id where Student_Id = {};""".format(id)
        cursor.execute(native_query)
        print(f'Запрос о студенте id: {id}')
        response = cursor.fetchall()
        for row in response:
            print("ID Студента: ", row[0])
            print("Имя студента: ", row[1])
            print("ID школы: ", row[2])
            print("Название школы: ", row[3])
        db_close(connection)
    except (Exception, sqlite3.Error) as error:
        print("Ошибка при выполнении запроса", error)



def inf_student1(id):
    try:
        connection = db_connect()
        cursor = connection.cursor()
        native_query = """select Students.Student_Id, Students.Student_Name, Students.School_Id, School.School_Name 
        from Students, School where Students.School_Id = School.School_Id and Students.Student_Id = {};""".format(id)
        cursor.execute(native_query)
        print(f'Запрос о студенте id: {id}')
        response = cursor.fetchall()
        for row in response:
            print("ID Студента: ", row[0])
            print("Имя студента: ", row[1])
            print("ID школы: ", row[2])
            print("Название школы: ", row[3])
        db_close(connection)
    except (Exception, sqlite3.Error) as error:
        print("Ошибка при выполнении запроса", error)


# create_db_table()
# data_for_db_table()
# inf_student(203)
inf_student1(203)


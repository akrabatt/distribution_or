import sqlite3
import os
import time

data_base = '/test_data_base.db'
table = 'clients_base'
file = 'test.txt'


def database_print_list(data_base, table, column_name=None):
    con = sqlite3.connect('test_data_base.db')  # конектимся с БД
    cur = con.cursor()  # создаём объект курсор для дальнейшей работы с ним
    query_name = 'pragma table_info(' + table + ')'  # узнаем наименование колонок
    cur.execute(query_name)  # выполняем query_name
    column_des = cur.fetchall()  # получаем данные
    if column_name is None:  # если имя колонки не задано
        query = 'SELECT * FROM ' + table  # все записи из всек колонок из таблицы
        cur.execute(query)
        data = cur.fetchall()
    # print(data)
    file_database = open('test.txt', 'w')
    for i in range(len(data)):
        file_database.write('\n')
        # file_database.write(data[i][0])
        for b in range(len(data[i])):
            file_database.write(data[i][b])
            file_database.write(' ')

    file_database.close()
    cur.close()
    con.close()
    os.startfile('test.txt')
    time.sleep(1)
    os.remove('test.txt')


if __name__ == '__main__':
    database_print_list(data_base, table)

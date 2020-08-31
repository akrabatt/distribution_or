import sqlite3

data_base = '/test_data_base.db'
table = 'clients_base'
emailes =[]
phones = []


def request_bd(data_base, table, column_name = None):
    con = sqlite3.connect('test_data_base.db')  # конектимся с БД
    cur = con.cursor()  # создаём объект курсор для дальнейшей работы с ним
    query_name = 'pragma table_info('+table+')'  # узнаем наименование колонок
    cur.execute(query_name)  # выполняем query_name
    column_des = cur.fetchall()  # получаем данные
    # print(column_des)
    if column_name is None:  # если имя колонки не задано
        query = 'SELECT * FROM '+table  # все записи из всек колонок из таблицы
        cur.execute(query)
        data = cur.fetchall()
    # print(data)
    for i in range(len(data)):
        emailes.append(data[i][2])
        phones.append(data[i][3])
    print(emailes, phones)
    cur.close()
    con.close()


if __name__ == '__main__':
    request_bd(data_base, table)

import sqlite3

"""ОБЯЗАТЕЛЬНО ПРИ РАБОТЕ С СУБД СОЕДИНЯЕМСЯ С БАЗоЙ И СОЗДАЕМ КУРСОР"""


def create_db():  # создаем функцию по созданию БД
    con = sqlite3.connect('test_data_base.db')  # создаём БД
    cur = con.cursor()  # создаём объект курсор для дальнейшей работы с ним
    cur.execute("CREATE TABLE IF NOT EXISTS clients_base(name TEXT,"  # если таблицы не существует, то создаем ее
                                                        "sername TEXT,"  # создаем в ней колонки
                                                        "email TEXT,"
                                                        "phone TEXT)")
    data = []  # пустой список для пополнения бызы данных
    name = input('введите имя: ')
    data.append(name)
    sername = input('введите фамилию: ')
    data.append(sername)
    email = input('введите email : ')
    data.append(email)
    phone = input('введите мобильный телефон: ')
    data.append(phone)

    cur.execute('INSERT INTO clients_base VALUES(?, ?, ?, ?)', data)  # добавляем все элементы по колонкам из списка в БД
    con.commit()
    cur.close()
    con.close()


if __name__ == '__main__':
    create_db()

# -*- config: UTF-8 -*-
import sqlite3

def create_db():  # создаем функцию по созданию БД
    con = sqlite3.connect('test_data_base.db')  # создаём БД
    cur = con.cursor()  # создаём объект курсор для дальнейшей работы с ним
    cur.execute("CREATE TABLE IF NOT EXISTS clients_base(name TEXT,"
                                                        "sername TEXT,"
                                                        "email TEXT,"
                                                        "phone TEXT)")
    data = []
    name = input('введите имя: ')
    data.append(name)
    sername = input('введите фамилию: ')
    data.append(sername)
    email = input('введите email : ')
    data.append(email)
    phone = input('введите мобильный телефон: ')
    data.append(phone)

    cur.execute('INSERT INTO clients_base VALUES(?, ?, ?, ?)', data)
    con.commit()
    cur.close()
    con.close()


create_db()



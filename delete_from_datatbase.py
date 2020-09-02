import sqlite3

def delete_from_db():
    print('Введите имя и фамилию клиента, которого хотите удалить')
    del_name = input('имя: ')
    del_sername = input('фамилию: ')
    con = sqlite3.connect('test_data_base.db')  # конектимся с БД
    cur = con.cursor()  # создаём объект курсор для дальнейшей работы с ним
    delete = "DELETE FROM clients_base WHERE name = '{0}' AND sername = '{1}'".format(del_name, del_sername)

    cur.execute(delete)
    con.commit()
    cur.close()
    con.close()


if __name__ == '__main__':
    delete_from_db()

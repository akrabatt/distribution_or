import  add_to_database
import request_from_database
import delete_from_datatbase

data_base = '/test_data_base.db'
table = 'clients_base'

print('введите 1 если хотите выполнить добавить клиента в базу')
print('введите 2 если хотите просмотреть базу клиентов')
print('введите 3 если хотите удалить клиента из базы')
print('введите 4 если  хотите вывести список клиентской базы')

num = input('введите цифру: ')
num = int(num)

if num == 1:
    add_to_database.create_db()
elif num == 2:
    request_from_database.request_bd(data_base=data_base, table=table)
elif num == 3:
    delete_from_datatbase.delete_from_db()
elif num ==4:
    pass
else:
    print('вы ввели неверное значение')
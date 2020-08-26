import smtplib  # модуль по работе с SMTP протоколом
from email.mime.multipart import MIMEMultipart  # Многокомпонентный объект
from email.mime.text import MIMEText  # Текст/HTML
from email.mime.image import MIMEImage  # Изображения

# Starwars-1999@yandex.ru
# workdakrabatt@gmail.com

addr_from = 'Starwars-1999@yandex.ru'  # отправитель
addr_to = 'workdakrabatt@gmail.com'  # получатель
password = '89114559170DIMa'

msg = MIMEMultipart()  # создаём сообщение
msg['From'] = addr_from  # адресат
msg['To'] = addr_to  # получатель
msg['Subject'] = 'Тема сообщения123'

body = 'Проверка соединения(не отвечать)'
msg.attach(MIMEText(body, 'plain'))  # добавляем сообщение в текст

server = smtplib.SMTP('smtp.yandex.ru', 587)
server.set_debuglevel(True)  # Включаем режим отладки - если отчет не нужен, строку можно закомментировать
server.starttls()  # шифровка и обмен по TLS
server.login(addr_from, password)
server.send_message(msg)
server.quit()
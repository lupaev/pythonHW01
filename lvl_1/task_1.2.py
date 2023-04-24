import random
import time
import datetime

def convert_to_sec(list) -> int:
    '''Функция конвертирования списка чисел тип float в целое число,
    преобразование в секунды.
    Параметры функции - float = []
    Результат функции - целое число тип int
    '''
    new_s = []
    for el in list:
        number = '{:.2f}'.format(el)
        new_s.append(str(number)) #получен список строк со временем

    new_str_list = []
    for el in new_s:
        new_str_list.extend(el.split("."))  # разделение на минуты и секунды и
        # создание одного списка
    m = []
    s = []
    for index in range(len(new_str_list)):
        if index % 2 == 0:
            m.append(new_str_list[
                         index])  # выделение минут из общего списка в отдельный
        else:
            s.append(new_str_list[
                         index])  # выделение секунд из общего списка в отдельный
    m1 = []
    for el in m:
        m1.append(int(el) * 60)
    s1 = []
    for el in s:
        s1.append(int(el))
    return sum(m1) + sum(s1) #сложение секунд


def conver_sec_to_time(sec: int) -> str:
    '''Функция преобразование секунд в строку в формат времени.
    Параметры функции - целое число тип int
    Результат функции - строка тип str
    '''
    return time.strftime('%M:%S', time.gmtime(sec))

# Задача 1.2.
# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]


list_song = random.sample(my_favorite_songs, 3)
s = []
for x in list_song:
    s.append(x[-1])
print(f'Три песни звучат {conver_sec_to_time(convert_to_sec(s))} минут')

# Пункт B.
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

random_t = random.sample(list(my_favorite_songs_dict.values()), 3)


print(f'Три песни звучат {conver_sec_to_time(convert_to_sec(random_t))} минут')

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# A
list_song_random = random.sample(my_favorite_songs, 3)
list_song2 = []
for x in list_song_random:
    list_song2.append(x[0])
print(list_song2)

# B
random_songs = random.sample(list(my_favorite_songs_dict.keys()), 3)
print(random_songs)

# Дополнительно
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

date_now = datetime.datetime.now()
print(date_now.strftime('%M minuts %S seconds'))


# Интересный вариант
# У меня был немного покороче

from random import sample
from datetime import timedelta
from math import modf

# Пункт D(А)
total_time = timedelta()
for song in sample(my_favorite_songs, 3):
    s, m = modf(song[1])
    total_time += timedelta(minutes=int(m), seconds=int(s * 100))

print(f'Пункт D(A): Три песни звучат {total_time}')

# Пункт D(B)
total_time = timedelta()
for song in sample(tuple(my_favorite_songs_dict), 3):
    s, m = modf(my_favorite_songs_dict[song])
    total_time += timedelta(minutes=int(m), seconds=int(s * 100))

print(f'Пункт D(B): Три песни звучат {total_time}')


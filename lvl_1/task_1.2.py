import random
import datetime
import time

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


list = random.sample(my_favorite_songs, 3)
s = []
for x in list:
    s.append(x[-1])
print(f'Три песни звучат {sum(s)} минут')

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

time = []
for key, value in my_favorite_songs_dict.items():
    time.append(value)
random_time = random.sample(time, 3)
print(f'Три песни звучат {sum(random_time)} минут')

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# A
list_song = random.sample(my_favorite_songs, 3)
list_song = []
for x in list:
    list_song.append(x[0])
print(list_song)

# B
list_song1 = []
for key, value in my_favorite_songs_dict.items():
    list_song1.append(key)
random_songs = random.sample(list_song1, 3)
print(random_songs)

# Дополнительно
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 


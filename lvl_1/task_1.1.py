# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

# 1 вариант
print(my_favorite_songs[:14], my_favorite_songs[-13:], my_favorite_songs[16:23] + my_favorite_songs[24:30], my_favorite_songs[-26:-15])
# Вывод: Waste a Moment  New Salvation Staying Alive Start Me Up

# 2 вариант
my_favorite_songs = my_favorite_songs.replace("'", '').split(', ')
print(my_favorite_songs[0], my_favorite_songs[-1], my_favorite_songs[1], my_favorite_songs[-2])
# Вывод: Waste a Moment  New Salvation Staying Alive Start Me Up
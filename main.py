import random
import time

def convert_to_sec(list) -> int:
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
    return time.strftime('%M:%S', time.gmtime(sec))


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

t = []
for key, value in my_favorite_songs_dict.items():
    t.append(value)
random_time = random.sample(t, 3)
print(random_time)
d = convert_to_sec(random_time)

print(f'Три песни звучат {conver_sec_to_time(d)} минут')
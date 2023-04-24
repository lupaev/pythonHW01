# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

def quarter_of(month):
    if month > 0 and month < 4:
        return 1
    elif month > 3 and month < 7:
        return 2
    elif month > 6 and month < 10:
        return 3
    elif month > 9 and month < 13:
        return 4
    else:
        return "Такого месяца нет"


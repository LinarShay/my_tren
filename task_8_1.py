def add_everything_up(a, b):
    try:
        # Попробуем сложить два объекта
        return a + b
    except TypeError:
        # Если типы различны, возвращаем строковое представление двух объектов
        return str(a) + str(b)

# Примеры вызовов функции
print(add_everything_up(123.456, 'строка'))  # 123.456строка
print(add_everything_up('персик', 4215))     # персик4215
print(add_everything_up(123.456, 7))         # 130.456

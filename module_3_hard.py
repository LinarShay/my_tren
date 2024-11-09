def calculate_structure_sum(data):
    total_sum = 0
    total_length = 0

    # Функция для рекурсивного обхода структур
    def recursive_sum(element):
        nonlocal total_sum, total_length

        if isinstance(element, int):  # Если элемент - целое число
            total_sum += element
        elif isinstance(element, str):  # Если элемент - строка
            total_length += len(element)
        elif isinstance(element, (list, tuple, set)):  # Если элемент - список, кортеж или множество
            for item in element:
                recursive_sum(item)
        elif isinstance(element, dict):  # Если элемент - словарь
            for key, value in element.items():
                recursive_sum(key)
                recursive_sum(value)

    # Запуск рекурсивной функции для начального уровня структуры
    recursive_sum(data)

    # Возвращаем результат как сумму чисел и общую длину строк
    return {'сумма чисел': total_sum, 'общая длина строки': total_length}


# Тестовые данные
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

# Запуск функции и вывод результата
result = calculate_structure_sum(data_structure)
print(result)
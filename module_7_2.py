def custom_write(file_name, strings):
    # Создаем пустой словарь для хранения позиций
    strings_positions = {}

    # Открываем файл в режиме записи с указанием кодировки utf-8
    with open(file_name, 'w', encoding='utf-8') as file:
        for line_number, string in enumerate(strings, start=1):
            # Получаем текущую позицию в файле перед записью строки
            byte_position = file.tell()

            # Записываем строку в файл, добавляя символ новой строки
            file.write(string + '\n')

            # Добавляем информацию в словарь: ключ - кортеж (номер строки, позиция), значение - строка
            strings_positions[(line_number, byte_position)] = string

    # Возвращаем словарь с позициями
    return strings_positions


# Пример использования функции
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)

# Вывод результата
for elem in result.items():
    print(elem)
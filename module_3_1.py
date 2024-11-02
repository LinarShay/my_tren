calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()  # Увеличиваем счётчик при вызове функции
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счётчик при вызове функции
    # Приводим строку и элементы списка к нижнему регистру для проверки
    return string.lower() in [item.lower() for item in list_to_search]

print(string_info("Hello"))        # Должно вывести (5, 'HELLO', 'hello')
print(is_contains("urban", ["city", "Urban", "village"]))  # Должно вывести True
print(is_contains("town", ["city", "Urban", "village"]))   # Должно вывести False

print("Количество вызовов функций:", calls)
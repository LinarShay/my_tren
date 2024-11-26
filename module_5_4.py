class House:
    # Атрибут класса для хранения истории построенных зданий
    houses_history = []

    def __new__(cls, *args, **kwargs):
        # Добавляем название здания в историю
        if len(args) > 0:  # Проверяем, передано ли имя здания
            cls.houses_history.append(args[0])
        return super().__new__(cls)  # Создаем новый объект

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        # Вывод сообщения при удалении объекта
        print(f"{self.name} снесён, но он останется в истории")

    def __str__(self):
        # Строковое представление объекта
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

# Пример использования
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)  # ['ЖК Эльбрус']

h2 = House('ЖК Акация', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация']

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# Удаление объектов
del h2
del h3

print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# Удаление последнего объекта
del h1

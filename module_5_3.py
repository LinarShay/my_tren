class House:
    def __init__(self, name, number_of_floors):
        """Инициализация объекта дома."""
        self.name = name  # Название дома
        self.number_of_floors = number_of_floors  # Количество этажей

    def __len__(self):
        """Возвращает количество этажей здания."""
        return self.number_of_floors

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        """Сравнение домов на равенство по количеству этажей."""
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __lt__(self, other):
        """Сравнение количества этажей (меньше)."""
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False

    def __le__(self, other):
        """Сравнение количества этажей (меньше или равно)."""
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return False

    def __gt__(self, other):
        """Сравнение количества этажей (больше)."""
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return False

    def __ge__(self, other):
        """Сравнение количества этажей (больше или равно)."""
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return False

    def __ne__(self, other):
        """Сравнение количества этажей (неравенство)."""
        return not self == other

    def __add__(self, value):
        """Увеличение количества этажей."""
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __radd__(self, value):
        """Сложение числа и объекта (работает как __add__)."""
        return self.__add__(value)

    def __iadd__(self, value):
        """Увеличение этажей через +=."""
        return self.__add__(value)


# Пример использования
h1 = House("ЖК Эльбрус", 10)
h2 = House("ЖК Акация", 20)

# Вывод строкового представления
print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 10
print(h2)  # Название: ЖК Акация, кол-во этажей: 20

# Сравнение
print(h1 == h2)  # False (__eq__)

# Увеличение этажей
h1 = h1 + 10  # __add__
print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 20

print(h1 == h2)  # True (__eq__)

h1 += 10  # __iadd__
print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 30

h2 = 10 + h2  # __radd__
print(h2)  # Название: ЖК Акация, кол-во этажей: 30

# Сравнение этажей
print(h1 > h2)  # False (__gt__)
print(h1 >= h2)  # True (__ge__)
print(h1 < h2)  # False (__lt__)
print(h1 <= h2)  # True (__le__)
print(h1 != h2)  # False (__ne__)

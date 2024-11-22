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


# Создаем объекты домов
h1 = House("ЖК Эльбрус", 10)
h2 = House("ЖК Акация", 20)

# Используем магические методы
# __str__
print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 10
print(h2)  # Название: ЖК Акация, кол-во этажей: 20

# __len__
print(len(h1))  # 10
print(len(h2))  # 20

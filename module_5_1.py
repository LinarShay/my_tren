class House:
    def __init__(self, name, number_of_floors):
        """Инициализация объекта дома."""
        self.name = name  # Название дома
        self.number_of_floors = number_of_floors  # Количество этажей

    def go_to(self, new_floor):
        """
        Перемещает на указанный этаж, выводя в консоль последовательность.
        Если этаж недоступен, выводит предупреждение.
        """
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(f"Этаж {floor}")
        else:
            print("Такого этажа не существует")


# Создание объекта дома
my_house = House("ЖК Эльбрус", 30)

# Вызов метода go_to
my_house.go_to(5)  # Пример: переезд на 5 этаж
my_house.go_to(31)  # Пример: недопустимый этаж
my_house.go_to(0)  # Пример: этаж меньше 1

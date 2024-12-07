# animal_plant_hierarchy.py

class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True  # Живой по умолчанию
        self.fed = False   # Не кормленный по умолчанию

    def eat(self, food):
        if isinstance(food, Plant):  # Убедимся, что food - это растение
            if food.edible:  # Если съедобно
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:  # Если несъедобно
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False
        else:
            print(f"{self.name} не может есть {food}, это не растение!")

class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False  # Несъедобное по умолчанию

class Mammal(Animal):
    pass  # Поведение полностью унаследовано от Animal

class Predator(Animal):
    pass  # Поведение полностью унаследовано от Animal

class Flower(Plant):
    pass  # Несъедобность остается неизменной

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Фрукты съедобны

# Тестирование работы программы
if __name__ == "__main__":
    # Создание объектов
    a1 = Predator('Тигр Сибири')
    a2 = Mammal('Белый медведь')
    p1 = Flower('Роза пустыни')
    p2 = Fruit('Сладкий ананас')

    # Проверка названий
    print(a1.name)  # Тигр Сибири
    print(p1.name)  # Роза пустыни

    # Проверка начальных атрибутов
    print(a1.alive)  # True
    print(a2.fed)    # False

    # Питание животных
    a1.eat(p1)  # Тигр Сибири не стал есть Роза пустыни
    a2.eat(p2)  # Белый медведь съел Сладкий ананас

    # Проверка финальных атрибутов
    print(a1.alive)  # False
    print(a2.fed)    # True

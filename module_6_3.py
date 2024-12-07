# duckbill.py

import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]  # Координаты (x, y, z)
        self.speed = speed  # Скорость движения

    def move(self, dx, dy, dz):
        new_z = self._cords[2] + dz * self.speed
        if new_z < 0:
            print("Слишком глубоко, я не могу нырнуть :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] = new_z

    def get_cords(self):
        print(f"X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
                print("Будьте осторожны, я атакую вас 0_0")

    def speak(self):
        if self.sound:
            print(self.sound)
        else:
            print("...")

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        eggs = random.randint(1, 4)
        print(f"Вот вам {eggs} яиц")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = abs(dz)  # Убедимся, что dz положительное
        new_z = self._cords[2] - dz * (self.speed / 2)
        if new_z < 0:
            print("Слишком глубоко, я не могу нырнуть :(")
        else:
            self._cords[2] = new_z

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Клик-клик-клик"

    def __init__(self, speed):
        super().__init__(speed)

# Тестирование работы программы
if __name__ == "__main__":
    db = Duckbill(10)  # Скорость утконоса 10

    # Проверка базовых атрибутов
    print(db.live)  # True
    print(db.beak)  # True

    # Утконос говорит и атакует
    db.speak()  # Клик-клик-клик
    db.attack()  # Будьте осторожны, я атакую вас 0_0

    # Утконос перемещается
    db.move(1, 2, 3)
    db.get_cords()  # X: 10 Y: 20 Z: 30

    # Утконос ныряет
    db.dive_in(6)
    db.get_cords()  # X: 10 Y: 20 Z: 0

    # Утконос откладывает яйца
    db.lay_eggs()  # Вот вам N яиц (N = 1-4)

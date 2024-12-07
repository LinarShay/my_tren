# geometric_shapes.py

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color)
        self.filled = True
        self.__sides = (
            list(sides)
            if self._is_valid_sides(*sides) and len(sides) == self.sides_count
            else [1] * self.sides_count
        )

    def _is_valid_color(self, r, g, b):
        return all(isinstance(c, int) and 0 <= c <= 255 for c in (r, g, b))

    def set_color(self, r, g, b):
        if self._is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print("Цвет не изменён, некорректные значения.")

    def get_color(self):
        return self.__color

    def _is_valid_sides(self, *sides):
        return all(isinstance(side, (int, float)) and side > 0 for side in sides)

    def set_sides(self, *new_sides):
        if self._is_valid_sides(*new_sides) and len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)
        else:
            print("Стороны не изменены, некорректные значения.")

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * 3.141592653589793)  # Используем значение pi

    def get_square(self):
        return 3.141592653589793 * (self.__radius**2)  # Используем значение pi


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        sides = self.get_sides()
        s = sum(sides) / 2
        return self._sqrt(s * (s - sides[0]) * (s - sides[1]) * (s - sides[2]))

    def _sqrt(self, value):
        """Вычисление квадратного корня вручную методом Ньютона."""
        guess = value / 2.0
        for _ in range(10):  # 10 итераций для точности
            guess = (guess + value / guess) / 2.0
        return guess


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        side = sides[0] if len(sides) == 1 and super()._is_valid_sides(sides[0]) else 1
        super().__init__(color, *([side] * self.sides_count))

    def get_volume(self):
        side = self.get_sides()[0]
        return side**3


# Тестирование работы программы
if __name__ == "__main__":
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка изменения цветов
    circle1.set_color(55, 66, 77)
    print(circle1.get_color())  # [55, 66, 77]

    cube1.set_color(300, 70, 15)
    print(cube1.get_color())  # [222, 35, 130]

    # Проверка изменения сторон
    cube1.set_sides(5, 3, 12, 4, 5)
    print(cube1.get_sides())  # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]

    circle1.set_sides(15)
    print(circle1.get_sides())  # [15]

    # Проверка периметра круга (длина окружности)
    print(len(circle1))  # 15

    # Проверка объёма куба
    print(cube1.get_volume())  # 216

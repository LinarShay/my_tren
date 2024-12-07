class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner  # Владелец может изменяться
        self.__model = model  # Модель, нельзя менять напрямую
        self.__engine_power = engine_power  # Мощность двигателя, нельзя менять напрямую
        self.__color = color.lower() if color.lower() in self.__COLOR_VARIANTS else 'undefined'

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color.capitalize()}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color.lower()
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def get_passenger_limit(self):
        return f"Лимит пассажиров: {self.__PASSENGERS_LIMIT}"


# Тестирование
if __name__ == "__main__":
    # Создание объекта Sedan
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

    # Изначальные свойства
    vehicle1.print_info()

    # Изменение цвета
    vehicle1.set_color('Pink')  # Недопустимый цвет
    vehicle1.set_color('BLACK')  # Допустимый цвет

    # Изменение владельца
    vehicle1.owner = 'Vasyok'

    # Проверка обновленных свойств
    vehicle1.print_info()

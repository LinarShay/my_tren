import threading
import time

class Knight(threading.Thread):
    """
    Класс Knight, представляющий рыцаря, сражающегося с врагами.
    Наследуется от класса Thread.
    """
    print_lock = threading.Lock()  # Блокировка для синхронизации вывода в консоль

    def __init__(self, name, power, enemies=100):
        """
        Инициализация рыцаря.
        :param name: Имя рыцаря.
        :param power: Сила рыцаря.
        :param enemies: Количество врагов.
        """
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = enemies

    def run(self):
        """
        Метод, выполняющийся при запуске потока.
        """
        with Knight.print_lock:
            print(f"{self.name}, на нас напали!")

        days = 0
        while self.enemies > 0:
            # Задержка в 1 секунду
            time.sleep(1)
            days += 1
            self.enemies -= self.power
            self.enemies = max(self.enemies, 0)  # Убедимся, что врагов не меньше 0

            # Синхронизируем вывод в консоль
            with Knight.print_lock:
                print(f"{self.name}, сражается {days} день(дня)..., осталось {self.enemies} воинов.")

        # После победы
        with Knight.print_lock:
            print(f"{self.name} одержал победу спустя {days} день(дня)!")


# Создаем двух рыцарей
first_knight = Knight("Sir Lancelot", 10, 100)  # У каждого рыцаря 100 врагов
second_knight = Knight("Sir Galahad", 20, 100)

# Запускаем потоки
first_knight.start()
second_knight.start()

# Ждем завершения потоков
first_knight.join()
second_knight.join()

# Выводим сообщение об окончании битв
with Knight.print_lock:
    print("Все битвы закончились!")

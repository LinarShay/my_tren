class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        # Формат строки: "<название>, <вес>, <категория>"
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        # Устанавливаем файл для хранения товаров
        self.file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.file_name, 'r') as file:
                # Считываем все строки из файла
                return file.read().strip()  # Удаляем лишние символы перехода строки
        except FileNotFoundError:
            # Если файла нет, возвращаем пустую строку
            return ""

    def add(self, *products):
        # Получаем текущие продукты из файла
        current_products = self.get_products()
        existing_names = {
            line.split(', ')[0]
            for line in current_products.split('\n') if line
        }

        with open(self.file_name, 'a') as file:
            for product in products:
                if product.name in existing_names:
                    print(f"Продукт {product.name} уже есть в магазине")
                else:
                    # Добавляем новый продукт в файл
                    file.write(str(product) + '\n')
                    existing_names.add(product.name)


# Пример работы программы
if __name__ == "__main__":
    s1 = Shop()

    p1 = Product ('Potato', 50.5, 'Vegetables')
    p2 = Product ('Spaghetti', 3.4, 'Groceries')
    p3 = Product ('Potato', 5.5, 'Vegetables')

    print(p2)  # Вывод строки: Spaghetti, 3.4, Groceries

    s1.add(p1, p2, p3)

    print(s1.get_products())
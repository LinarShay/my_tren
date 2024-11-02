def print_params(a=1, b="строка", c=True):
    print("a =", a)
    print("b =", b)
    print("c =", c)

print("Вызов без аргументов:")
print_params()

print("\nВызов с одним именованным аргументом (b = 25):")
print_params(b=25)

print("\nВызов с одним именованным аргументом (c = [1, 2, 3]):")
print_params(c=[1, 2, 3])

values_list = [10, "example", False]
values_dict = {"a": 3.14, "b": "распакованное значение", "c": None}

print("\nРаспаковка из списка:")
print_params(*values_list)

print("\nРаспаковка из словаря:")
print_params(**values_dict)

values_list_2 = ["распаковка с добавлением", False]

print("\nРаспаковка с отдельным параметром (42):")
print_params(*values_list_2, 42)
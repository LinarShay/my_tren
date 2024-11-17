def test_funktion():
    def inner_funktion():
        print("Я в функции test_funktion")

    inner_funktion()

test_funktion()

try:
    inner_funktion()
except NameError as e:
    print(f"Ошибка: {e}")
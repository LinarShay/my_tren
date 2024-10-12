# 1st program
result = (9 ** 0.5) * 5
print('результат №1',result)
# 2nd program
result = 9.99 > 9.98 and 1000 != 1000.1
print('результат №2',result)
# 3rd program
result1 = 2 * 2 + 2 # Выражение без приоритета

result2 = 2 * (2 + 2) # Выражение с приоритетом для сложения

comparison = result1 == result2 # Сравнение результатов

print('Выражение без приоритета: ' ,result1)  # Результат: 6
print('Выражение c приоритетом:' ,result2)  # Результат: 8
print('Сравнение: ',comparison)  # Результат: False
# 4th program
number_str = '123.456'
number = float(number_str)
number_shifted=int(number*10)
first4 = number_shifted %10
print('результат №4',first4)
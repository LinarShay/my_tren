def find_pairs(n):
    result = ""

    for i in range(1, 21):

        for j in range(i + 1, 21):

            if n % (i + j) == 0:

                result += str(i) + str(j)
    return result

n = 11
result = find_pairs(n)
print(f"Для числа {n} подходящие пары: {result}")

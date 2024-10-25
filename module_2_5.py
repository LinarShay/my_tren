def get_matrix(n, m, value):
    matrix = []

    for _ in range(n):
        row = [value] * m
        matrix.append(row)

    return matrix

result1 = get_matrix(3, 5, 24)
result2 = get_matrix(4, 2, 42)
result3 = get_matrix(5, 4, 29)

print(result1)
print(result2)
print(result3)

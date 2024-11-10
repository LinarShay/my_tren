from fake_math import divide as fake_divide
from true_math import divide as true_divide

result1 = fake_divide(33, 3)
result2 = fake_divide(6, 0)
result3 = true_divide(77, 7)
result4 = true_divide(13, 0)

print(result1)
print(result2)
print(result3)
print(result4)
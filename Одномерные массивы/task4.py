
import random

inp = int(input('Укажите размер массива: '))
a = []
b = []
c = []
for i in range(inp):
    a.append(random.randint(1, 5))
    b.append(random.randint(1, 5))
print('Исходный массив #1\n' + str(a))
# print(a)
print('Исходный массив #2\n' + str(b))
# print(b)
for i in range(inp):
    c.append(a[i] * b[(inp-1)-i])
print('Преобразованный массив\n' + str(c))


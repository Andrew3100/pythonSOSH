# Сформировать два массива случайных целых чисел от 1 до 100.
# Перебором массива в цикле умножить первый элемент исходного первого массива на
# последний элемент исходного второго массива (и так далее по всем элементам).
# Конечный массив вывести в терминал
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

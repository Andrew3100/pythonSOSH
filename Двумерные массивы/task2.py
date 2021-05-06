# Задача:
# Создать многомерный массив из случайных целых чисел.
# Транспонировать массив. Вывести транспонированный массив,
# каждый элемент которого является произведением исходного элемента на диагональный элемент этой строки.
import random
inp = int(input(("Укажите размер массива")))
# Наполнение матрицы случайными элементами
matrix = [[random.randint(10, 99) for j in range(inp)] for i in range(inp)]
# Вывод наполненной матрицы на экран
print('Исходная матрица: \n')
for i in range(inp):
    for g in range(inp):
        print((matrix[i][g]), end=' ')
    print('\n')
# Транспонирование матрицы. Заполнение матрицы по строкам, но противоположными индексами
transpose = [[matrix[j][i] for j in range(inp)] for i in range(inp)]

diagonal = []
print('Транспонированная матрица: \n')
# Вывод транспонированной матрицы на экран
for i in range(len(transpose)):
    for g in range(len(transpose)):
        print(transpose[i][g], end=' ')
        # Проверка на диагональный элемент
        if i == g:
            diagonal.append(transpose[i][g])
    print('\n')
# Вывод массива диагоналей
print('Массив диагоналей')
print(diagonal)
print('\n')
print('Изменённая матрица')
# Проход транспонированной матрицы и умножение каждого элемента на диагональ этой строки
for i in range(len(transpose)):
    for g in range(len(transpose)):
        print(transpose[i][g] * diagonal[i], end=' ')
    print('\n')
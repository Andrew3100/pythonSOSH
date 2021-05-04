# Задача:
# Сформировать массив случайных целых чисел от 1 до 100.
# Каждый чётный элемент массива умножить на случайное значение в диапазоне от этого элемента до 100.
# Каждый нечётный элемент умножить на случайное значение в
# диапазоне от минимального значения до максимального в этом массиве.
# Результаты записать и вывести в два разных массива

import random

len_array = int(input('Укажите размер массива: '))
array = []
new_array = []
for i in range(len_array):
    array.append(random.randint(0, 100))

print(array)


for i in range(len_array):
    if array[i] % 2 == 0:
        r = random.randint(array[i], 100)
        print('Умножаю число ' + str(array[i]) + ' на число ' + str(r) + ' из диапазона от ' + str((array[i])) + ' до 100')
        new_array.append(array[i] * r)
    else:
        rr = random.randint(min(array), max(array))
        print('Умножаю число ' + str(array[i]) + ' на число ' + str(rr) + ' из диапазона от ' + str(min(array)) + ' до ' + str(max(array)))
        new_array.append(array[i] * rr)

print(new_array)
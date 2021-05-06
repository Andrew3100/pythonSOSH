# Задача:
#     Указать размер массива вводом с клавиатуры. Сгенерировать рандомный массив целых чисел заданного размера.
#     В этом массиве найти наибольший и наименьший элемент.
#     Сформировать случайный массив и перемножить его элементы на наибольшее из первого массива.
#     Сформировать второй массив и выполнить умножение на минимальное значение
# Решение:
# Для генерации случайных элементов подключаем модуль для работы рандома
import random

# Объявляем три массива, первичный и два других требуемых по задаче
array = []
array_multiplication_by_maximum_value = []
array_multiplication_by_minimum_value = []

arr_size = int(input('Укажите размер массива: '))
arr_max = int(input('Укажите диапазон наибольшего значения: '))
min = arr_max
max = 0

# Заполнение первичного массива длиной arr_size случайными целыми числами в диапазоне от 1 до arr_max
for i in range(arr_size):
    array.append(random.randint(1, arr_max))
print(array)
# Проход первичного массива
for i in range(arr_size):
    # Если текущий элемент больше текущего максимума,
    # то максимум обновляем. На первом шаге сравниваем текущий элемент с нулём
    if array[i] > max:
        max = array[i]
    # Если текущий элемент меньше текущего минимума,
    # то минимум обновляем. На первом шаге сравниваем текущий элемент со значением arr_max
    if array[i] < min:
        min = array[i]
print('Максимальное значение ' + str(max))
print('Минимальное значение ' + str(min))
for i in range(arr_size):
    array_multiplication_by_maximum_value.append((array[i] * max))
    array_multiplication_by_minimum_value.append((array[i] * min))
print('Массив произведений на максимум ' + str(array_multiplication_by_maximum_value))
print('Массив произведений на минимум ' + str(array_multiplication_by_minimum_value))

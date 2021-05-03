# Задача:
#     Указать размер массива вводом с клавиатуры.
#     Сгенерировать рандомный массив целых чисел заданного размера.
#     Записать в отдельные массивы чётные и нечётные числа.
#     Элементы данных массивов вывести в терминал.


# Для генерации случайных элементов подключаем модуль для работы рандома
import random

# Объявляем три массива, первичный и два других требуемых по задаче
array = []
array_of_even_numbers = []
array_of_uneven_numbers = []

arr_size = int(input('Укажите размер массива: '))

# Заполнение первичного массива длиной arr_size случайными целыми числами
for i in range(arr_size):
    array.append(random.randint(1, 100))

# Проход первичного массива
for i in range(arr_size):
    if array[i] % 2 == 0:
        array_of_even_numbers.append(array[i])
    else:
        array_of_uneven_numbers.append(array[i])

print(array_of_even_numbers)
print(array_of_uneven_numbers)

print('В первом массиве ' + str(len(array_of_even_numbers)) + ' символов')
print('Во втором массиве ' + str(len(array_of_uneven_numbers)) + ' символов')
print('Процентное соотношение  - ' + str(round(len(array_of_even_numbers) / arr_size * 100)) + '% чётных символов и '
      + str(round(len(array_of_uneven_numbers) / arr_size * 100)) + '% нечётных символов')


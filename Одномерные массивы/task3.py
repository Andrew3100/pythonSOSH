# Задача:
#     Сформировать случайный массив целых чисел.
#     Пока в массиве не попалось трёхзначное число – перемножаем элементы на максимум этого массива.
#     Трёхзначное число не трогаем, а все числа после него перемножаем на минимум из этого массива.
#     Всё вывести в терминал
import random
# Объявляем 2 массива, первичный и два других требуемых по задаче
array = []
new_arr = []
arr_size = int(input('Укажите размер массива: '))
# Контрольная точка
spot = ''
# Заполнение первичного массива длиной arr_size
for i in range(arr_size):
    array.append(random.randint(1, 120))
index = 0
# Бежим по массиву пока не попадается первое трёхзначное число
while len(str(array[index])) != 3:
    new_arr.append(array[index] * max(array))
    index += 1
# Как только оно попалось, запоминаем индекс этого элемента в массиве
fixed = index
# Бежим по массиву начиная с этого индекса и до конца
for i in range(fixed, len(array)):
    if array[i] == array[fixed]:
        new_arr.append(array[i])
    else:
        new_arr.append(array[i] * min(array))
print(array)
print(new_arr)

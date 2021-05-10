import io
import time
import math
start = time.time()
print('Введите ник: ')
word = input()
res = []
with io.open('telegram_clear_data.txt', encoding='windows-1251') as file:
    i = 0
    g = 0
    search = 0
    krat = 400000
    for line in file:
        i = i+1
        if i % krat == 0:
            print('Поиск завершён на ', search, '%\r')
            search = search + 1
        if word in line:
            g = g + 1
            res.append(line)

    print('Поиск пользователей завершён. По Вашему запросу было найдено', g, ' пользователей')
    print('Поиск пользователей завершён. Было проверено', i, ' строк файла')
    stop = time.time()
    time = stop - start
    print('Весь файл я обошёл за ' + str(round(time)) + ' секунд')
    print('За секунду я проверяю' + str(round(i / time)) + ' строк')















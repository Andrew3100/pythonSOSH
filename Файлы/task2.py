import io

print('Введите ник: ')
word = input()
with io.open('telegram_clear_data.txt', encoding='windows-1251') as file:
    i = 0
    g = 0
    search = 0
    krat = 400000
    for line in file:
        i = i+1
        if i % krat == 0:
            print('Поиск завершён на ', search, '/100 процентов')
            search = search + 1
        if word in line:
            g = g + 1
            # print(line, end='')

    print('Поиск пользователей завершён. По Вашему запросу было найдено', g, ' пользователей')
    print('Поиск пользователей завершён. Было проверено>', i, ' строк файла')

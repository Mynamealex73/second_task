born_year = input("Введите год рождения А.С. Пушкина: ")
if int(born_year) == 1799:
    print('Верно!')
    born_day = input('А теперь введите день рождения А.С. Пушкина (только число): ')
    if int(born_day) == 6:
        print('Верно!')
    else:
        print('Неверно!')
else:
    print('Неверный год рождения!')

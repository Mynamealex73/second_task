sum_a = 0
sum_b = 0
answer = None

while answer !='нет':
    # Чарли Чаплин - 1889
    chaplin_born_year = int(input("Введите год рождения Чарли Чаплина: "))
    if chaplin_born_year == 1889:
        sum_a +=1
    else:
        sum_b +=1

    # Юрий Алексеевич Гагарин - 1934
    gagarin_born_year = int(input("Введите год рождения Ю.А. Гагарина: "))
    if gagarin_born_year == 1934:
        sum_a +=1
    else:
        sum_b +=1

    # Александр Сергеевич Пушкин - 1799
    pyshkin_born_year = int(input("Введите год рождения А.С. Пушкина: "))
    if pyshkin_born_year == 1799:
        sum_a +=1
    else:
        sum_b +=1

    # Альберт Эйнштейн - 1879
    einstein_born_year = int(input("Введите год рождения Альберта Эйштейна: "))
    if einstein_born_year == 1879:
        sum_a +=1
    else:
        sum_b +=1

    # Никола Тесла - 1856
    tesla_born_year = int(input("Введите год рождения Николы Тесла: "))
    if tesla_born_year == 1856:
        sum_a +=1
    else:
        sum_b +=1
    # Лев Николаевич Толстой - 1828
    tolstoi_born_year = int(input("Введите год рождения Л.Н. Толстого: "))
    if tolstoi_born_year == 1828:
        sum_a +=1
    else:
        sum_b +=1
    # Нельсон Мандела - 1918
    mandela_born_year = int(input("Введите год рождения Нельсана Манделы: "))
    if mandela_born_year == 1918:
        sum_a +=1
    else:
        sum_b +=1

    proc_a = (sum_a * 100) / 7
    proc_b = (sum_b * 100) / 7

    print('Колличество правильных ответов: ', sum_a)
    print('Колличество неправильных ответов: ', sum_b)
    print('Процент правильных ответов: ', proc_a, '%')
    print('Процент неправильных ответов: ', proc_b, '%')

    answer = input('Хотите начать игру сначала (да/нет)?: ')

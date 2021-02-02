# 1 Задание
try:
    x = 0  # Начальная точка x
    y = 0  # Начальная точка y
    kladx = int(input())  # Клад находится по оси запад-восток
    klady = int(input())  # Клад находится по оси север-юг
    word = str(input())  # Слово — одно из набора: «вперёд», «налево», «направо», «разворот» или «стоп».
    counter_of_action = 0  # Счетчик действий
    side = 'север'  # Изначальное направление
    while word != 'стоп':  # Цикл работает до тех пор пока, пользователь не напишет 'стоп'
        if word == 'вперед':  # Оператор работает с добавлением шагов от зависимости от направления
            steps = int(input())
            counter_of_action += 1
            if side == 'север':
                y += steps
            elif side == 'юг':
                y -= steps
            elif side == 'запад':
                x -= steps
            elif side == 'восток':
                x += steps
        elif word == 'налево':  # Оператор работает с изменением направления стороны налево
            if side == 'север':
                side = 'запад'
                counter_of_action += 1
            elif side == 'запад':
                side = 'юг'
                counter_of_action += 1
            elif side == 'юг':
                side = 'восток'
                counter_of_action += 1
            elif side == 'восток':
                side = 'север'
                counter_of_action += 1
        elif word == 'направо':  # Оператор работает с изменением направления стороны направо
            if side == 'север':
                side = 'восток'
                counter_of_action += 1
            elif side == 'восток':
                side = 'юг'
                counter_of_action += 1
            elif side == 'юг':
                side = 'запад'
                counter_of_action += 1
            elif side == 'запад':
                side = 'север'
                counter_of_action += 1
        elif word == 'разворот':  # Оператор работает с изменением направления стороны на противоложную
            if side == 'север':
                side = 'юг'
                counter_of_action += 1
            elif side == 'запад':
                side = 'восток'
                counter_of_action += 1
            elif side == 'юг':
                side = 'север'
                counter_of_action += 1
            elif side == 'восток':
                side = 'запад'
                counter_of_action += 1
        word = str(input())
    if x == kladx and y == klady:  # Проверка координат клада и нашей
        print(counter_of_action)
        print(side)
    else:
        print(0)
except (ValueError, TypeError):
    print('Error occurred')


# 2 Задание
try:
    d = int(input())  # День
    m = int(input())  # Месяц
    year = int(input())  # Год
    if m - 2 > 0:  # Оператор вычисляет сдвиг месяца на 2 назад
        year = year
        m = m - 2
    else:  # Если if не прошел, то мы убираем 1 год и считаем месяц
        year -= 1
        m = 12 - abs(m - 2)
    y = year % 100  # Считает год столетия
    c = year // 100  # Считает столетия
    print((d + ((13*m - 1) // 5) + y + (y // 4 + c // 4 - (2*c) + 777)) % 7)  # Формула вычисления дня недели по заданию
except TypeError:
    print('Wrong type')

# 3 Задание
try:
    word = str(input())
    # Есть такой хороший оператор - извлечения среза. [BEGIN:END:STEP]
    print(word[2])  # Выводит 3 символ строки
    print(word[-2])  # Выводит предпоследний символ строки
    print(word[:5])  # Выводит первые 5 символов строки
    print(word[:-2])  # Выводит все символы кроме последних двух
    print(word[::2])  # Выводит все символы с четными индексами(начиная с 0)
    print(word[1::2])  # Выводит все символы с нечетными индексами
    print(word[::-1])  # Выводит все символы в обратном порадке
    print(word[::-2])  # Выводит все символы строки через 1 в обратном порядке, начиная с конца
    print(len(word))  # Выводит длину строки
except TypeError:
    print('Wrong Type')

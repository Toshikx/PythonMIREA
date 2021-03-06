def f21(x):
    if x[0] =='elm':
        return 12
    elif x[0] == 'kit':
        if x[2] == 'oz':
            if x[1] == 1962:
                return 9
            elif x[1] == 1984:
                return 10
            elif x[1] == 1997:
                return 11
        if x[2] == 'ats':
            if x[1] == 1962:
                return 6
            elif x[1] == 1984:
                return 7
            elif x[1] == 1997:
                return 8
    elif x[0] == 'gams':
        if x[1] == 1997:
            if x[2] == 'ats':
                return 4
            elif x[2] == 'oz':
                return 5
        elif x[1] == 1984:
            if x[3] == 2003:
                return 3
            elif x[3] == 1997:
                return 2
        elif x[1] == 1962:
            if x[3] == 2003:
                return 1
            elif x[3] == 1997:
                return 0
#if-else table
def f221(number):
    a = number & 0b00000000000000001111111111111111
    b = number & 0b00111111111111110000000000000000
    c = number & 0b11000000000000000000000000000000
    b = b >> 16
    c = c >> 30
    numb = (a << 16) | (b << 2) | c
    return numb
#working transcoder in format of task

persones1 = [
    ['+7 (172) 581-48-63', '+7 (172) 581-48-63', 'Мирон К. Гетук!0.0', 'Нет'],
    ['+7 (223) 002-48-29', '+7 (223) 002-48-29', 'Арсений Ш. Шавунов!0.0', 'Да'],
    [None, None, None, None],
    ['+7 (223) 002-48-29', '+7 (223) 002-48-29', 'Арсений Ш. Шавунов!0.2', 'Да'],
    ['+7 (223) 002-48-29', '+7 (223) 002-48-29', 'Арсений Ш. Шавунов!0.2', 'Да'],
    ['+7 (399) 031-52-20', '+7 (399) 031-52-20', 'Павел М. Гумберг!0.6', 'Нет'],
    ['+7 (973) 400-93-02', '+7 (973) 400-93-02', 'Адель И. Деволко!0.2', 'Нет' ],

]

persones2 = [
    ['+7 (934) 092-91-96', '+7 (934) 092-91-96', 'Давид И. Субиди!0.7', 'Нет'],
    ['+7 (861) 387-57-68', '+7 (861) 387-57-68', 'Давид Н. Шомулов!0.2', 'Да'],
    ['+7 (861) 387-57-68', '+7 (861) 387-57-68', 'Давид Н. Шомулов!0.2', 'Да'],
    ['', '', '', ''],
    ['+7 (250) 080-82-88', '+7 (250) 080-82-88', 'Рамиль Е. Цедин!0.7', 'Да'],
    ['+7 (861) 387-57-68', '+7 (861) 387-57-68', 'Давид Н. Шомулов!0.2', 'Да'],
]

persones3 = [
    ['+7 (861) 387-57-68', '+7 (861) 387-57-68', 'Давид Н. Шомулов!0.2', 'Да'],
    [None, None, None, None],
    ['+7 (250) 080-82-88', '+7 (250) 080-82-88', 'Рамиль Е. Цедин!0.7', 'Да'],
    ['+7 (861) 387-57-68', '+7 (861) 387-57-68', 'Давид Н. Шомулов!0.2', 'Да']
]

def f23(x):
    #Создание списка без повторов
    y = []
    for i in x:
        if i not in y:
            y.append(i)

    #Удаление дубликатов в 1 и 2 строке
    for column in y:
        if column[0] == column[1]:
            del column[1]


    # Удаление пустых строк
    for line in y:
        for str in line:
            if str == None:
                y.pop(y.index(line))
                break

    #Преобразование строк
    for line in y:
        new = ''
        str = line[0]
        line[0] = str[9:] #Обрезание первых строк номера
        procent = line[1]
        procent = procent[-1: len(procent)]
        name = line[1]
        yesNo = line[2]
        if procent == '0':
            line[1] = '0%'
        else:
            line[1] = procent[-1: len(procent)] + '0%'

        if yesNo == 'Нет':
            line[2] = '0'
        elif yesNo == 'Да':
            line[2] = '1'
        for i in name: #Работа со строкой для формата
            if i == ' ':
                new = name[0:1]
                newStr = name[name.index(i):len(name)]
                new += '.' + name[name.index(i)+1:name.index(i)+3]
                newStr = newStr[newStr.index(i)+4:len(newStr)-4]
                new += ' ' + newStr

        line.append(new)

    #Сортировка строк
    y = sorted(y, key=lambda x: x[2], reverse=True)
    y.sort()


    return y

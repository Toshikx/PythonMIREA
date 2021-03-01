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
def f22(number):
    a = number & 0b00000000000000001111111111111111
    b = number & 0b00111111111111110000000000000000
    c = number & 0b11000000000000000000000000000000
    b = b >> 16
    c = c >> 30
    numb = (a << 16) | (b << 2) | c
    return numb
#working transcoder in format of task
def f23(table):
    #table function in progress
    return table
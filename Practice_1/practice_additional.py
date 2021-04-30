def __twenty_multiple_with_pluses__(x):
    x = x+x+x
    x = x + x
    x = x + x
    return x
print()
print("Умножение на 12. Сложением 4 раза.")
print("f({0}) = {1}".format(1,__twenty_multiple_with_pluses__(1)))
print("f({0}) = {1}".format(2,__twenty_multiple_with_pluses__(2)))
print("f({0}) = {1}".format(3,__twenty_multiple_with_pluses__(3)))
print("f({0}) = {1}".format(6,__twenty_multiple_with_pluses__(6)))

def __sixteen_multiple_with_pluses__(x):
    x =  x+x
    x = x + x
    x =  x+x
    x = x + x
    return x
print()
print("Умножение на 16. Сложением 4 раза.")
print("f({0}) = {1}".format(1,__sixteen_multiple_with_pluses__(1)))
print("f({0}) = {1}".format(2,__sixteen_multiple_with_pluses__(2)))
print("f({0}) = {1}".format(3,__sixteen_multiple_with_pluses__(3)))
print("f({0}) = {1}".format(6,__sixteen_multiple_with_pluses__(6)))

def __fifteen_multiple_with_pluses__(x):
    a = x + x
    a = a + a
    a = a + a
    a = a + a
    x = a - x
    return x
print()
print("Умножение на 15. Сложением 4 раза и минусованием 1 раз.")
print("f({0}) = {1}".format(1,__fifteen_multiple_with_pluses__(1)))
print("f({0}) = {1}".format(2,__fifteen_multiple_with_pluses__(2)))
print("f({0}) = {1}".format(3,__fifteen_multiple_with_pluses__(3)))
print("f({0}) = {1}".format(6,__fifteen_multiple_with_pluses__(6)))


def __twentynine_multiple_with_pluses__(x):
    a = x + x
    a = a + a
    a = a + x
    a = a+a+a
    x = a+a-x
    return x
print()
print("Умножение на 29. Сложением 6 раз и 1 вычитанием.")
print("f({0}) = {1}".format(1,__twentynine_multiple_with_pluses__(1)))
print("f({0}) = {1}".format(2,__twentynine_multiple_with_pluses__(2)))
print("f({0}) = {1}".format(3,__twentynine_multiple_with_pluses__(3)))
print("f({0}) = {1}".format(6,__twentynine_multiple_with_pluses__(6)))


#SyntaxError: cannot assign to literal
#можно получить при именовании строки с цифры    1 = 'Нет - ****** ответ!'

#SyntaxError: invalid syntax
#можно получить к примеру на разных версиях питона, к примеру данная запись
# print(f'DEBUG: {e}')
#при использовании python2 выдаёт ошибку

#NameError: name ... is not defined
#
#можно не задать значение переменной, при этом используя её в дальнейшем
#k == 1
#if k == 0:
#   month = input()
#print(month)

#TypeError: unsupported operand type(s) for ...
#x = input()
#v = x-tan(2)
#оператор - не работает для 'str' и 'float'

#IndentationError: expected an indented block
#появялется при неверной табуляции
#if z == 1:
#print(a)

#ZeroDivisionError: division by zero
#деление на ноль
#x = 0
#y = 0
#z = x/y

#ValueError: math domain error
#def f(x):
#    f = zeros(len(x))
#    f[0] = sin(x[0]) + x[1]**2 + log(x[2]) - 7.0
#    f[1] = 3.0*x[0] + 2.0**x[1] - x[2]**3 + 1.0
#    f[2] = x[0] + x[1] + x[2] -5.0
#    return f
# x = array([1.0, 1.0, 1.0])
# print newtonRaphson2(f,x)

#OverflowError: math range error
#math.exp(710)
#переполнение математической функции


print(" \nИсправление операции умножения naive_mul : ")
def naive_mul(x, y):
   if y == 0:
       return 0
   r = x
   for i in range(y-1):
       x = x + r
   return x

for i in range(101):
    print(f'\n{15} multiple {i} is {naive_mul(15,i)}')

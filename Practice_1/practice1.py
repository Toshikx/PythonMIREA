import math


def f11(x, y, z):
    first = ((math.e**z - math.cos(y)) / (z + ((x ** 2) / 36) - 79))
    firstSqrt = math.sqrt(first)
    second = ((math.cos(x) + (y ** 4) - 43) / (
            (56 * y) - (12 * y ** 6)))
    third = (math.tan(x) + (26 * x ** 7))
    return (firstSqrt + second - third);


def f12(x):
    if x < 94:
        return 87*x**6 - math.log(x) - 29*x**8
    elif 94 <= x < 139:
        return x - 47*x**5+94
    elif 139 <= x < 206:
        return x**2 + math.cos(x)
    elif x>=206:
        return math.fabs(math.cos(x**3-x**7-83)) - x**6


# print(foo2(75))
# print(foo2(167))


def f13(n, m):
    sum2 = 0
    def fooSum():
        sum = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                sum+=50*(math.log(i)+math.log(j)-14)
        return sum
    for i in range(1, n+1):
        sum2+=80*i**5+math.sin(i)
    result = fooSum() - sum2
    return result

# print(foo3(31, 81))
# print(foo3(81, 83))

def f14(n):
    if n == 0:
        return 3
    ans = (1/30)*f14(n-1)-math.sin(f14(n-1))
    return ans

# print(foo4(2))
# print(foo4(11))


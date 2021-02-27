import math


class func_quadratica:
    def __init__(self) -> None: pass

    def calcula_raiz(self, a, b, c) -> tuple:
        raiz = self.__calc_delta(a, b, c)

        x1 = (-b + raiz)/(2*a)
        x2 = (-b - raiz)/(2*a)

        return (x1, x2)

    def __calc_delta(self, a, b, c) -> float:
        return math.sqrt(b**2 - 4*a*c)


a = float(input())
b = float(input())
c = float(input())

print(func_quadratica().calcula_raiz(a, b, c))

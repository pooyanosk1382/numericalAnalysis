import math


def f(x):  # define main function (cos(x) + x)
    return math.cos(x) + x


def g(x):  # define differential function of cos(x) + x (1 - sin(x))
    return 1 - math.sin(x)


def mainAlgo(x):  # calculate ten times the Newton algorithm
    for i in range(10):
        x = x - (f(x) / g(x))
    return x


x = int(input("Enter your first guess : "))
print(mainAlgo(x))

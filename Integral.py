import math


def solveSin():  # define integral of function sin(x)
    print("Enter the number of trapezium:")
    n = int(input())
    a = 1  # starting point of interval
    b = 2  # end point of interval
    h = (b - a) / n
    s = 0
    while a < b:
        temp = a + h
        s += ((math.sin(a) + math.sin(temp)) * h) / 2  # surface of each trapezium
        a = temp
    return s


def solveExpon():  # define integral of function e^(-(x^2))
    print("Enter the number of trapezium:")
    n = int(input())
    a = 0  # starting point of interval
    b = 1  # end point of interval
    h = (b - a) / n
    s = 0
    while a < b:
        temp = a + h
        s += ((math.e**(-(a**2)) + math.e**(-(temp**2))) * h) / 2  # surface of each trapezium
        a = temp
    return s


print("Which one do you want to see its integral?")
print("1.Sin(x) from 1 to 2")
print("2.e^(x^(-2)) from 0 to 1")
x = int(input())
if x == 1:
    print(solveSin())
elif x == 2:
    print(solveExpon())
else:
    print("Invalid input")
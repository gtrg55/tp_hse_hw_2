
import pytest

import time
import math
from statistics import mean
time_start = time.time()
mas = []
with open("mas.txt") as f:

    for i in f:

        mas.append(int(i))


print(mas)


def maxx():
    return max(mas)
def minn():
    return min(mas)

def summ():
    sum = 0

    for i in range(len(mas)):
        b = int(mas[i])
        sum = sum + b
    return sum
def avg():
    return round(mean(mas))


def multt():
    mult = 1
    for i in range(len(mas)):
        b = int(mas[i])
        mult = mult * b

    return mult


print("Сумма", summ())
print("Произведение", multt())
print("Минимальное", minn())
print("Максимальное", maxx())
print("Среднее значение массива ", avg())
time_end = time_start - time.time()
print("Расчет занял", (abs(round(time_end, 5))), "секунд")
def test_multt_good():
    test_mult = 1
    for i in range(len(mas)):
        b = int(mas[i])
        test_mult = test_mult * b
    #print(test_sum)
    assert multt() == test_mult
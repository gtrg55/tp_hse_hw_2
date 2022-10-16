import time
from ast import literal_eval as le
import math
from statistics import mean
time_start = time.time()
mas = []
mas2= []
with open("mas.txt") as f:
    mas.append(f.read().split())
    mas = str(mas)


    mas = mas[2:-2]



mas = le(mas)
for i in range(len(mas)):
    mas2.append(int(mas[i]))


print(mas2)
def maxx():
    return max(mas)
print("Максимальное", maxx())
time_end = time_start - time.time()
print("Расчет занял", (abs(round(time_end, 5))), "секунд")
time_start = time.time()


def minn():
    return min(mas)
print("Минимальное", minn())

time_end = time_start - time.time()
print("Расчет занял", (abs(round(time_end, 5))), "секунд")
time_start = time.time()
def summ():
    sum = 0

    for i in range(len(mas)):
        b = int(mas[i])
        sum = sum + b
    return sum
print("Сумма", summ())
time_end = time_start - time.time()
print("Расчет занял", (abs(round(time_end, 5))), "секунд")
time_start = time.time()
def avg():
    return round(mean(mas2))

print("Среднее значение массива ", avg())
time_end = time_start - time.time()
print("Расчет занял", (abs(round(time_end, 5))), "секунд")
time_start = time.time()


def multt():
    mult = 1
    for i in range(len(mas)):
        b = int(mas[i])
        mult = mult * b

    return mult
print("Произведение", multt())
time_end = time_start - time.time()
print("Расчет занял", (abs(round(time_end, 5))), "секунд")
time_start = time.time()






'''
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат 
заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
'''

import random
result = []

startarr = [random.randint(1,100) for _ in range(20)]
print(f'Исходный массив: {startarr}')

minrange = int(input("Введите минимум диапазона (число от 1 до 100): "))
maxrange = int(input("Введите максимум диапазона (число от 1 до 100): "))

for el in startarr:
    if (el > minrange and el < maxrange):
        result.append(el)

print(f'Результирующий массив: {result}')        


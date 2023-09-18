
'''
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
'''
import os

print("Текущая деректория:", os.getcwd())

f = open(os.getcwd()+'\LESS4\config.txt','r')

max = 0;

try:
   # работа с файлом
   contentvals = f.readline().split(' ');
   if (len(contentvals)):
        sum = int(contentvals[len(contentvals)-3]) + int(contentvals[len(contentvals)-2]) + int(contentvals[len(contentvals) - 1])
        print(f"NUMS = {contentvals[len(contentvals)-3]} {contentvals[len(contentvals)-2]} {int(contentvals[len(contentvals) - 1])}")
   for i in range(len(contentvals)-1):
        sum = int(contentvals[i-1]) + int(contentvals[i]) + int(contentvals[i + 1])
        print(f"NUMS = {contentvals[i-1]} {contentvals[i]} {contentvals[i + 1]}")
        if (sum > max):
            max = sum
   
   print(f"максимальное числа ягод = {max}")
finally:
   f.close()

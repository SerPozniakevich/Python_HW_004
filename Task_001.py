#Вычислить число c заданной точностью d
# #Пример:
#при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}

from ast import While
import math

num_pi = math.pi
d = input('Введите десятичную дробь с колличеством знаков после точки необходимой точности (пример: 0.001): ')
print(round(num_pi, len(str(d).split('.')[1][:])))
## делим введённую строку по точке, принимаем все значения второй части (индекс 1)
## и выводим пи с округлением до длинны стоки
## P.s. странно, что для комментирования в данном коде одной # не хватает.... 
#Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# k=4 => 2*x^4 + 4*x^3 + 5x^2  - 3x + 3 = 0

from random import random
from random import randint
import contextlib

k = int(input('Введите значение степени многочлена: '))
n = k
equation_list = []
x = ''
j = ''
g = ''
for i in range(k + 1):
    if k == 0:
        j = randint(0, 100)
        if j != 0:
            g = j
            equation_list.append(g)
        elif j == 0:
            continue
    if k == 1:
        j = randint(0, 100)
        if j != 0:
            g = (f'{j}*x')
            equation_list.append(g)
        elif j == 1:
            equation_list.append('x')
        elif j == 0:
            continue
    if k > 1:
        j = randint(0, 100)
        if j != 0:
            g = (f'{j}*x^{k}')
            equation_list.append(g)
        elif j == 1:
            equation_list.append(x^{k})
        elif j == 0:
            continue
    k -=1


print(f'k={n} =>', end=' ')
print (' + '.join(map(str, equation_list)), end=' = 0')


# with open('file.txt', 'a') as data:
#     with contextlib.redirect_stdout(data):
#         print (' + '.join(map(str, equation_list)), end=' = 0\n')

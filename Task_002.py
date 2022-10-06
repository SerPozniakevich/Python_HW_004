# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

from distutils.command.build import build
from unittest import result


n = int(input('Ведите число: '))
set_buid = {}
set_buid = set(set_buid)

if n % 7 != 0 and n % 5 != 0 and n % 3 != 0 and n % 2 != 0:
    print(f'Число {n} не имеет простых множителей')
elif n % 7 == 0:
    n = n / 7
    set_buid.add(7)
elif n % 5 == 0:
    n = n / 5
    set_buid.add(5)
elif n % 3 == 0:
    n = n / 3
    set_buid.add(3)
elif n % 2 == 0:
    n = n / 2 
    set_buid.add(2)
    
print(set_buid)

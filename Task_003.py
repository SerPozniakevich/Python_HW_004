# 3адайте последовательность чисел. 
# Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

from itertools import count
from random import random
from random import randint
import copy
from multiprocessing.sharedctypes import Value
from random import shuffle
from unittest.mock import patch

n = int(input('Введите длину списка чисел: '))
list1 = []

for i in range(n):
    list1.append(randint(0, 5))
print(list1)
list2= set()

for i in range(1, len(list1)):
    for j in range(len(list1)):
        if j == i:
            continue
        if list1[j] == list1[i]:
            list2.add(list1[j])
# print(list2)
list1 = set(list1)
# print(list1)
list3 = list1.difference(list2)
print(list3)


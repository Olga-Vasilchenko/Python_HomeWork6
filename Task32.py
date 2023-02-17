# Задача 32:
# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума).

from random import randint
start, stop = [int(i) for i in input("Введите диапазон: ").split()]
list_num = [randint(-10, 10) for i in range(randint(10, 20))]
print(list_num, [i for i, n in enumerate(list_num) if n in range(start, stop+1)], sep="\n")

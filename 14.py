# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k),
# не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input())
a = int(2)
degree = 0
c = 0
while c * a <= n:
    c = a ** degree
    print(c, end=' ')
    degree = degree + 1
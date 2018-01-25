#!usr/bin/env python
# -*- Coding: UTF-8 -*-

from sys import stdout

if __name__ == '__main__':
    a = []
    for i in range(10):
        a.append([])
        # print(a)
        for j in range(10):
            a[i].append(0)

    for i in range(10):
        a[i][0] = 1
        a[i][i] = 1

    for i in range(2,10):
        for j in range(1, i):
            a[i][j] = a[i - 1][j - 1] + a[i - 1][j]

    for i in range(10):
        for j in range(i + 1):
            stdout.write(str(a[i][j]))
            stdout.write(' ')
        print()

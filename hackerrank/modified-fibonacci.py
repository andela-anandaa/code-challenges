'''
Source: https://www.hackerrank.com/challenges/fibonacci-modified
'''

import sys

for line in sys.stdin:
    x = line

a, b, c = [int(i) for i in x.split()]

def fib(n):
    if n == 3:
        return a + b**2
    elif n == 2:
        return b
    elif n == 1:
        return a
    return fib(n - 2) + (fib(n - 1))**2

print(fib(c))


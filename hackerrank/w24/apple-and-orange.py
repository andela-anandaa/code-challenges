#!/bin/python

'''
Source: https://www.hackerrank.com/contests/w24/challenges/apple-and-orange
'''
import sys


s, t = raw_input().strip().split(' ')
s, t = [int(s), int(t)]
a, b = raw_input().strip().split(' ')
a, b = [int(a), int(b)]
m, n = raw_input().strip().split(' ')
m, n = [int(m), int(n)]
apple = map(int, raw_input().strip().split(' '))
orange = map(int, raw_input().strip().split(' '))

apple_count = 0
orange_count = 0

for i in apple:
    distance = a + i
    if distance >= s and distance <= t:
        apple_count += 1

for i in orange:
    distance = b + i
    if distance >= s and distance <= t:
        orange_count += 1

print apple_count
print orange_count

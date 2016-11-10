'''
Source:https://www.hackerrank.com/challenges/camelcase
'''
import sys

s = raw_input().strip()

wc = 1 # since first word is lowercase

for letter in s:
    if letter.isupper():
        wc += 1

print wc

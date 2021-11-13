#!/usr/bin/env python3
# -*- coding: utf-8 -*-#!


import sys


s = input('Write something: ')
if s.count(' ') == len(s) or len(s) == 0:
    print("There are no text", file=sys.stderr)
    exit(1)
i = s.count('a') + s.count('A')
perc = i * 100 / (len(s) -  s.count(' '))

print(f"Percentage of 'a' in your text is: {perc}%")

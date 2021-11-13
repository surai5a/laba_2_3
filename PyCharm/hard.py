#!/usr/bin/env python3
# -*- coding: utf-8 -*-#!


def check(s):
    if s.count(' ') == len(s) or len(s) == 0:
        print("There are no word", file=sys.stderr)
        exit(1)


s = (input("Your text: "))
check(s)

if (' k' or ' K') not in s:
    print("There are no word in text with first letter 'k'")
    exit(0)
else:
    ss = s.split()
    print("There are words with first 'k': ")
    for i in ss:
        if i[0] == 'k' or i[0] == 'K':
            print(i)
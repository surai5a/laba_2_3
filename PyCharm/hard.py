#!/usr/bin/env python3
# -*- coding: utf-8 -*-#!

import sys


def check(x):
    if x.count(' ') == len(x) or len(x) == 0:
        print("There are no word", file=sys.stderr)
        exit(1)


if __name__ == '__main__':
    s = (input("Your text: "))
    check(s)
    if ((' k' and ' к') not in s) and (s[0] != 'k' and s[0] != 'к'):
        print("There are no word in text with first letter 'k'")
        exit(0)
    else:
        ss = s.split()
        print("There are words with first 'k': ")
        for i in ss:
            if i[0] == 'k' or i[0] == 'к':
                print(i)

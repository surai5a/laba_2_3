#!/usr/bin/env python3
# -*- coding: utf-8 -*-#!

import sys

if __name__ == '__main__':
    s = input('Write something: ')
    if s.count(' ') == len(s) or len(s) == 0:
        print("There are no text", file=sys.stderr)
        exit(1)
    i = s.count('а') + s.count('А') + s.count('a') + s.count('A')
    percent = i * 100 / len(s)

    print(f"Percentage of 'a' in your text is: {percent}%")

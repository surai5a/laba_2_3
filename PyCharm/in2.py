#!/usr/bin/env python3
# -*- coding: utf-8 -*-#!

import sys


def check(x):
    if x.count(' ') == len(x) or len(x) == 0:
        print("There are no text", file=sys.stderr)
        exit(1)


if __name__ == '__main__':
    s = (input("Your text: "))
    check(s)
    if 'да' not in s:
        print("There are no 'да' in your text")
        exit(0)
    else:
        ss = s.replace("да", "не")
        print(f"Edited text: {ss}")


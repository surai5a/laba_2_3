#!/usr/bin/env python3
# -*- coding: utf-8 -*-#!

import sys


def check(x):
    if x.count(' ') == len(x) or len(x) == 0:
        print("There are no word", file=sys.stderr)
        exit(1)


if __name__ == '__main__':
    s = input("Your word: ")
    check(s)
    k = int(input("Number of letter you want to cut: "))
    t = int(input("Number of letter where you want to past: "))
    ch = s[k]
    s1 = s[:k]
    s2 = s[(k + 1):(t + 1)]
    s3 = s[(t + 1):]
    print("Edited word: ", s1 + s2 + ch + s3)

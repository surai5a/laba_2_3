#!/usr/bin/env python3
# -*- coding: utf-8 -*-#!


def check(s):
    if s.count(' ') == len(s) or len(s) == 0:
        print("There are no word", file=sys.stderr)
        exit(1)


s = input("Your word: ")
check(s)
k = int(input("Number of letter you want to cut: "))
l = int(input("Number of letter where you want to past: "))
ch = s[k]
s1 = s[:k]
s2 = s[(k + 1):(l + 1)]
s3 = s[(l + 1):]
print("Edited word: ", s1 + s2 + ch + s3)

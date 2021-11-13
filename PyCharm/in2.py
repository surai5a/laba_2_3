#!/usr/bin/env python3
# -*- coding: utf-8 -*-#!

import sys


def check(s):
    if s.count(' ') == len(s) or len(s) == 0:
        print("There are no text", file=sys.stderr)
        exit(1)


s = (input("Your text: "))
check(s)
if 'da' not in s:
    print("There are no 'da' in your text")
    exit(0)
else :
    ss = s.replace("da", "ne")
    print(f"Edited text: {ss}")


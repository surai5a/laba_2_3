#!/usr/bin/env python3
# -*- coding: utf-8 -*-#!

import sys


s = (input("Your text: "))

if s.count(',') == 0 :
    print("There is no ',' in your text", file=sys.stderr)
    exit(1)
else :
    es = ((s.partition(','))[0])
    n = es.count('n')
    N = es.count('N')
    print(f"{n+N} 'n' were found in your text")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-#!


def unique(s):
    es = s.partition(' ')
    z1 = len(es[0])
    z2 = len(es[2])
    w1 = es[0]
    w2 = es[2]
    list = set()
    f = 0
    for i in range(z1):
        f = 0
        for j in range(z2):
            if w1[i] == w2[j]:
                f = 1
        if f == 0:
            list.add(w1[i])
            yield w1[i]
    for i in range(z2):
        f = 0
        for j in range(z1):
            if w2[i] == w1[j]:
                f = 1
        if f == 0:
            list.add(w2[i])
            yield w2[i]


s = input("Your 2 words: ")
print("Unique letters for both: "(''.join(unique(s))))
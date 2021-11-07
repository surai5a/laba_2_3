#!/usr/bin/env python3
# -*- coding: utf-8 -*-#!


# def unique(it):
#     s = set()
#     for x in it:
#         if x not in s:
#            s.add(x)
#            # yield x
#     return(s)
#
# s = input("Your word: ")
# print(''.join(unique(s)))


def unique(it):
    s = []
    for x in it:
        if x not in s:
           s.append(x)
    return(s)

s = input("Your word: ")
print("Only unique letters: " + (''.join(unique(s))))

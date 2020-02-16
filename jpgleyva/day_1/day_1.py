#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 18:34:21 2019

@author: jpgleyva

"""
def part1():
    floor = 0
    
    lineList = [line.rstrip('\n') for line in open('input_day_1.txt')]
    
    for c in lineList[0]:
        if c == ")":
            floor -= 1
        else:
            floor += 1
    
    return floor


def part2():
    floor = 0
    position = 0
    lineList = [line.rstrip('\n') for line in open('input_day_1.txt')]
    
    for c in lineList[0]:
        if c == ")":
            floor -= 1
        else:
            floor += 1
        position += 1
        if floor == -1:
            break
    
    return position

print(part1())
print(part2())
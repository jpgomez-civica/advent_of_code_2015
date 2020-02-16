#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 19:12:51 2019

@author: jpgleyva
"""

def calc_paper(l,w,h):
    rest = min(l*w,l*h,w*h)
    total = (2*l*w)+(2*l*h)+(2*w*h)+rest
    return total

def calc_ribbon(data):
    wrap = data[0]+data[0]+data[1]+data[1]
    box = data[0]*data[1]*data[2]
    return wrap+box
    

def part1():
    lineList = [line.rstrip('\n') for line in open('input_day_2.txt')]
    papel_quantity = 0
    for o in lineList:
        l,w,h = o.split('x')
        papel_quantity += calc_paper(int(l), int(w), int(h))
    return papel_quantity

def part2():
    lineList = [line.rstrip('\n') for line in open('input_day_2.txt')]
    ribbon_quantity = 0
    for o in lineList:
        box = o.split('x')
        box_int = list(map(int, box))
        box_int.sort()
        data = list(filter(None, box_int)) 
        ribbon_quantity += calc_ribbon(data)
    return ribbon_quantity
    
#print(part1())
print(part2())
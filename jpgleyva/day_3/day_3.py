#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 20:00:55 2019

@author: jpgleyva
"""

p = {'x':0,'y':0}

def up(p):
    p['y'] += 1 
    return p
 
def down(p):
    p['y'] -= 1
    return p
 
def left(p):
    p['x'] -= 1
    return p

def right(p):
    p['x'] += 1
    return p
 

def part1(p):
    input = [line.rstrip('\n') for line in open('input_day_3.txt')]
    houses = []
    houses.append(p)
    
    for i in input[0]:
        new_p = {}
        if i == '^':
            new_p = up(p)
        elif i == 'v': 
            new_p = down(p)
        elif i == '<': 
            new_p = left(p)
        elif i == '>': 
            new_p = right(p)
        else:
            break
        p = new_p.copy()
        houses.append(p)  
        
    uniques = {}    
    for house in houses:
        k = str(house['x'])+','+str(house['y'])
        uniques[k] = True
    
    return len(uniques)





def part2(p):
    input = [line.rstrip('\n') for line in open('input_day_3.txt')]
    #input = '^v^v^v^v^v'
    houses = []
    houses.append(p)
    
    santa = p.copy()
    robot = p.copy()
    for index, i in enumerate(input[0]):
        if index%2 == 0:
            new_p = {}
            if i == '^':
                new_p = up(santa)
            elif i == 'v': 
                new_p = down(santa)
            elif i == '<': 
                new_p = left(santa)
            elif i == '>': 
                new_p = right(santa)
            else:
                break
            santa = new_p.copy()
            houses.append(new_p)
        else:
            new_p = {}
            if i == '^':
                new_p = up(robot)
            elif i == 'v': 
                new_p = down(robot)
            elif i == '<': 
                new_p = left(robot)
            elif i == '>': 
                new_p = right(robot)
            else:
                break
            robot = new_p.copy()
            houses.append(new_p)  
        
    uniques = {}  
    for house in houses:
        k = str(house['x'])+','+str(house['y'])
        uniques[k] = True
    
    return len(uniques)
    

#print(part1(p))
print(part2(p))
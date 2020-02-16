#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 18:51:32 2019

@author: jpgleyva
"""

def three_vowels(chain):
    count = 0
    for letter in chain.lower():
        if letter in ('a','e','i','o','u'):
            count += 1
    if count >= 3:
        return True
    else:
        return False
    
def twice_in_a_row(chain):
    dict = {}
    result = False
    for letter in ''.join(sorted(chain)):
        dict[letter] = chain.count(letter)
    for key,val in dict.items():
        if val >= 2:
            result = True
            break
    return result   

def twice_followed(chain):
    result = False
    for index, letter in enumerate(chain):
        if index+1 < len(chain):
            if letter == chain[index+1]:
                result = True
                break
    return result

def not_has_prohibited_substrings(chain):
    prohibited = ['ab','cd','pq','xy']
    result = True
    for index, letter in enumerate(chain):
        if index+1 < len(chain):
            substr = letter+chain[index+1]
            if substr in prohibited:
                result = False
                break
    return result

def repeat_between(chain):
    result = False
    for index, letter in enumerate(chain):
        if index+2 < len(chain):
            if letter == chain[index+2]:
                result = True
    return result

def two_letters_twice_without_overlaping(chain):
    result = False
    dict = {}
    for index, letter in enumerate(chain):
        if index+1 < len(chain):
            dict[chain[index]+chain[index+1]] = chain.count(chain[index]+chain[index+1])
    for key,val in dict.items():
        if val >= 2:
            result = True
            break
    return result 

        
def part1(lines):
    counter = 0
    lineList = [line.rstrip('\n') for line in open('input_day_5.txt')]
    
    for line in lineList:
        if three_vowels(line) and twice_followed(line) and not_has_prohibited_substrings(line):
            counter += 1
            lines.append(line)
            
    return counter

lines = []

#print(three_vowels('abeco'))
#print(twice_in_a_row('aeiouaeiouaeiou')) 
#print(has_prohibited_substrings('haegwjzuvuyxypyu'))

#print('Part 1 solution is {}'.format(part1(lines)))
#print(lines)

lines = []

def part2(lines):
    counter = 0
    lineList = [line.rstrip('\n') for line in open('input_day_5.txt')]
    
    for line in lineList:
        if repeat_between(line) and two_letters_twice_without_overlaping(line):
            counter += 1
            lines.append(line)
            
    return counter

print('Part 2 solution is {}'.format(part2(lines)))
print(lines)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 08:59:44 2019

@author: jpgleyva
"""

import hashlib 
  

def part1(secret,n):
    #secret = 'pqrstuv'
    answer = 1
    
    chain = secret + str(answer)
    
    substr = '11111'
    condition = '0'*n
    
    while substr != condition:
        result = hashlib.md5(chain.encode())
        substr = str(result.hexdigest())[0:n]
        answer += 1
        chain = secret + str(answer)
        
    return answer-1

#output1 = part1('ckczppom', 5)
#print('Output part 1 = {}'.format(output1))  

output2 = part1('ckczppom', 6)
print('Output part 2 = {}'.format(output2))  
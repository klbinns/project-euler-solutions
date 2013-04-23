#!/usr/bin/python
'''
Problem 1: 
Find the sum of all the multiples of 3 or 5 below 1000
'''

target = 1000
total = 0


for i in range(target):
    
    if (i % 3 == 0 or i % 5 == 0):
        total += i
            
print total # 233168

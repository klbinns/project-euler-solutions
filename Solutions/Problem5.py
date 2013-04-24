#!/usr/bin/python
import sys
'''
Problem 5:

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

# may be able to convert this to a recursive function

i = 20

while True:
    if i % 19 == 0:
        if i % 18 == 0:
            if i % 17 == 0:
                if i % 16 == 0:
                    if i % 15 == 0:
                        if i % 14 == 0:
                            if i % 13 == 0:
                                if i % 12 == 0:
                                    if i % 11 == 0:
                                        print i #232792560
                                        break
    i += 20


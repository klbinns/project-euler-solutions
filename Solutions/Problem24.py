#!/usr/bin/python
from itertools import permutations, islice
'''
Problem 24

A permutation is an ordered arrangement of objects. For example, 3124 is 
one possible permutation of the digits 1, 2, 3 and 4. If all of the
order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

'''
def nth(iterable, n, default=None):
        "Returns the nth item or a default value"
        return next(islice(iterable, n, None), default)
        
# nth function is zero indexed, hence 999999 - millionth element
answer = nth(permutations(range(10)), 999999)

print ''.join(map(str, answer)) # 2783915460
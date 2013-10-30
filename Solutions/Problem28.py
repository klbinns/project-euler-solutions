#!/usr/bin/python
import math
'''
Problem 28:

Starting with the number 1 and moving to the right in a clockwise direction
a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
formed in the same way?

'''
stop = 1001**2

idx = 1
space = 2
sum = 1

'''
There is a visible pattern that emerges when you draw out the grid in a
linear format.

Start index at 1, at index to sum, then:
do 4 times: increment index by 2, add index to sum
do 4 times: increment index by 4, add index to sum
do 4 times: increment index by 6, add index to sum
...and so on

You can stop when the number is the square of the grid size

'''

while idx < stop:
    for i in range(4):
        idx += space
        sum += idx
        
    space += 2 # the dist between diagonals increase by 2 after each iteration


print sum # 669171001




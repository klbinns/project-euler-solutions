import sys
'''
Problem 5:

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def isDivisible(n, divisor):
  return n % divisor == 0

def isRangeDivisble(n, y, x):
  return all(isDivisible(n, i) for i in range(y, x, -1))

i = 20

while True:
  if isRangeDivisble(i, 19, 10):
    print(i) # 232792560
    break
  else:
    i += 20

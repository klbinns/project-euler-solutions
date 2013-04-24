#!/usr/bin/python
import math
'''
Problem 7:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
'''


def isPrime(n):
    if n == 1:
        return False

    if n < 4:
        return True #2 and 3 are prime

    if n % 2 == 0:
        return False

    if n < 9:
        return True #we have already checked 4,6 and 8 via above

    if n % 3 == 0:
        return False

    r = math.floor(math.sqrt(n)) # n rounded to the greatest integer r so that r*r<=n
    f=5
    
    while f <= r:
        if n % f == 0: 
            return False 
        if n % (f+2) == 0:
            return False 
        f=f+6

    return True


# solve the problem here
limit = 10001
count = 1 
answer = 1

while not count == limit:
    answer = answer + 2
    if isPrime(answer):
        count += 1


print answer # 104743

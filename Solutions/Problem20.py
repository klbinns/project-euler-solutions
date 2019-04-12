import math

'''
Problem 20

Find the sum of the digits in the number 100!

'''

fact_100 = math.factorial(100)

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n /= 10
    return s

print(sum_digits(fact_100)) # 648

'''
Problem 16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

'''

a = 2**1000

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n /= 10
    return s

print(sum_digits(a)) # 1366

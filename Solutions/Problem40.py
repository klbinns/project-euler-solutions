from functools import reduce

'''
Problem 40:

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

'''

a = [str(x) for x in range(0, 1000000 +1)]
joined = ''.join(a)

d = [digit for digit in joined]

list_of_n = [1, 10, 100, 1000, 10000, 100000, 1000000]
solution = reduce(lambda acc, idx: acc * int(d[idx]), list_of_n, 1)

print(solution) # 210

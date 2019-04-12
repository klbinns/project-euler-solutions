from math import floor
'''
Problem 9:

A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''

s = 1000
a = 3

for a in range(3, floor((s-3)/3)):
    for b in range(a+1, floor((s-1-a)/2)):
        c = s-a-b
        if c*c == a*a + b*b:
            print(a, b, c)
            print ('Product: ' + str(a*b*c)) # 31875000
            
from itertools import permutations

'''
Problem 43:

The number, 1406357289, is a 0 to 9 pandigital number because it is made up 
of each of the digits 0 to 9 in some order, but it also has a rather 
interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we 
note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.

'''
    
combos = permutations(range(10))

def chunk_divisible(tup, start_idx, div_by):
    a = tup[start_idx:start_idx+3]
    t = int(''.join(map(str, a)))
    return True if t % div_by == 0 else False

sum = 0
for r in combos:
    test = True
    
    # Python will short circuit these evaluations
    test = test and chunk_divisible(r, 1, 2) 
    test = test and chunk_divisible(r, 2, 3)
    test = test and chunk_divisible(r, 3, 5)
    test = test and chunk_divisible(r, 4, 7)
    test = test and chunk_divisible(r, 5, 11)
    test = test and chunk_divisible(r, 6, 13)
    test = test and chunk_divisible(r, 7, 17)
    
    if test:
        t = int(''.join(map(str, r)))
        sum += t
    
print(sum) # 16695334890

# a bit slow using Python in serial fashion.
# I wonder if we can use parallel processing to speed things up?


import math
'''
Problem 10:

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

'''

# isPrime function from Problem 7
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
    
    
answer = 2 # since we know 2 is prime
limit = 2000000 # 2 million

# start at three, then go through odds only
for n in range(3, limit, 2):
    if isPrime(n):
        answer += n
            
            
print(answer) # 142913828922
# brute force solution, kinda slow
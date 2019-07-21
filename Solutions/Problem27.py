'''
Euler discovered the remarkable quadratic formula:
n^2+n+41
It turns out that the formula will produce 40 primes for the
consecutive integer values 0≤n≤39. However, when n=40,40^2+40+41=40(40+1)+41 is
divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.
The incredible formula n2−79n+1601 was discovered, which produces 80 primes for
the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.
Considering quadratics of the form:
n2+an+b, where |a| < 1000 and |b| ≤ 1000
where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that
produces the maximum number of primes for consecutive values of n, starting with n=0.
'''

def is_prime(x):
  if x > 1:
    isPrime = True
    for num in range(2, x):
      if x % num == 0:
        isPrime = False
        break
    return isPrime
  else:
    return False

def number_of_primes(a, b):
  n = 0
  primes = []
  while True:
    x = pow(n, 2) + (a*n) + b
    if is_prime(x):
      primes.append(x)
      n += 1
    else:
      break
  return len(primes)

a_max = 0
b_max = 0
max_num_of_primes = 0
for a in range(-1000, 1000):
  for b in range(-1000, 1001):
    n_o_p = number_of_primes(a, b)
    if n_o_p > max_num_of_primes:
      a_max = a
      b_max = b
      max_num_of_primes = n_o_p

print(a_max * b_max)

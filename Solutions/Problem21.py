'''
Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are
an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10,
11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
d_evals = {}
amicable_numbers = set()

def divisors(n):
  i = 1
  r = []
  while i < n:
    if n % i == 0:
      r.append(i)
    i += 1
  return r

def d(n):
  if n in d_evals:
    return d_evals[n]
  else:
    d_evals[n] = sum(divisors(n))
    return d_evals[n]

for a in range(1, 10001):
  b = d(a)
  if a != b and a == d(b):
    amicable_numbers.add(a)
    amicable_numbers.add(b)

print(sum(list(amicable_numbers))) # 31626

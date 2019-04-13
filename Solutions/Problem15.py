'''
Problem 15:

Starting in the top left corner of a 2×2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''

# cache previously traversed paths
cache = {}

def num_of_routes(x, y):
  if x == 0 and y == 0:
    return 1
  
  left = 0
  if x > 0:
    if (x-1, y) in cache:
      left = cache[(x-1, y)]
    else:
      left = num_of_routes(x-1, y)

  right = 0
  if y > 0:
    if (x, y-1) in cache:
      right = cache[(x, y-1)]
    else:
      right = num_of_routes(x, y-1)
  
  count = left + right
  cache[(x, y)] = count
  return count

print(num_of_routes(20, 20)) # 137846528820

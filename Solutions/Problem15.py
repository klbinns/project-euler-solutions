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
  if x == 0 or y == 0:
    return 1
  
  if (x, y) in cache:
    return cache[(x, y)]

  cache[(x, y)] = num_of_routes(x-1, y) + num_of_routes(x, y-1)
  return cache[(x, y)]  
  
print(num_of_routes(20, 20)) # 137846528820

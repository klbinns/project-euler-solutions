'''
Problem 25

What is the first term in the Fibonacci sequence to contain 1000 digits?

'''

a = 1
b = 1
c = 0
index = 2

while len(str(c)) < 1000:
  c = a + b
  index += 1 
  a = b
  b = c
 
print(index) #4782

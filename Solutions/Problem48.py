'''
Problem 48:

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

'''

# calculate all the factorials and sum (really wasteful, but easy to code)
s = sum([i**i for i in range(1,1001)])

#convert to string, print last 10 digits
print(str(s)[-10:]) # 9110846700

# There is undoubtedly a faster way (albeit, more lines of code) to do this.
# Something like filtering out or not calculating anything after the 11th digit
# i.e. calculate the exponentials and just keep the last 10 digits, this
# way we aren't keeping/calculting data that don't impact the end result

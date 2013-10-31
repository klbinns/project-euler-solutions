#!/usr/bin/python
import os
from math import sqrt

'''
Problem 42

The nth term of the sequence of triangle numbers is given by, tn = .5n(n+1); 
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its 
alphabetical position and adding these values we form a word value. For 
example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value
is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file 
containing nearly two-thousand common English words, how many are triangle 
words?

'''
#open file, read words
script_dir = os.path.dirname(__file__)
rel_path = 'data/words.txt'
abs_file_path = os.path.join(script_dir, rel_path)

file = open(abs_file_path, 'r')
words = file.read().translate(None, '"').split(",")


# compute word score function
def compute_word_score(word):
    return sum([(ord(char)-64) for char in word])

# test to see if argument is a triangle number
def is_triangle_number(score):
    n = (sqrt((8*score)+1)-1)/2
    return True if float(n).is_integer() else False
    
# compute score for each name
word_scores = [compute_word_score(word) for word in words]

# filter out tri_numbers
tri_numbers = [score for score in word_scores if is_triangle_number(score)]

# print length of tri_numbers list
print len(tri_numbers) # 162

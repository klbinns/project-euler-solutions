#!/usr/bin/python
import os

'''
Problem 22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into 
alphabetical order. Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain 
a name score.

For example, when the list is sorted into alphabetical order, COLIN, which 
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?

'''
#open file, read names
script_dir = os.path.dirname(__file__)
rel_path = 'data/names.txt'
abs_file_path = os.path.join(script_dir, rel_path)

file = open(abs_file_path, 'r')
names = file.read().translate(None, '"').split(",")

# sort names
names.sort()

# compute name score function
def compute_name_score(name):
    return sum([(ord(char)-64) for char in name])

# compute score for each name
name_scores = [compute_name_score(name) for name in names]

# compute score for each index * name: index * name_score
index_scores = [(idx+1)*val for idx, val in enumerate(name_scores)]

# sum scores and print
print sum(index_scores) # 871198282

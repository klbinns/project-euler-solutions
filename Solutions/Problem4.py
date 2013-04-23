#!/usr/bin/python
'''
Problem 4:

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def isPalindrome(x):
    x_str = str(x)
    return x_str == x_str[::-1]


largestPalindrome = 0
a = 999

while a >= 100:
    b = 999
    while b >= a:
        if a*b <= largestPalindrome:
            break;
            
        if isPalindrome(a*b):
            largestPalindrome = a*b
        
        b = b-1
        
    a = a-1
    
print largestPalindrome # 906609
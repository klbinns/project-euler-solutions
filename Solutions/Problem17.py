'''
If the numbers 1 to 5 are written out in words:
one, two, three, four, five, then there are
3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) 
inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters
and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
'''

lookup = {
  0: '',
  1: 'one',
  2: 'two',
  3: 'three',
  4: 'four',
  5: 'five',
  6: 'six',
  7: 'seven',
  8: 'eight',
  9: 'nine',
  10: 'ten',
  11: 'eleven',
  12: 'twelve',
  13: 'thirteen',
  14: 'fourteen',
  15: 'fifteen',
  16: 'sixteen',
  17: 'seventeen',
  18: 'eighteen',
  19: 'nineteen',
  20: 'twenty',
  30: 'thirty',
  40: 'forty',
  50: 'fifty',
  60: 'sixty',
  70: 'seventy',
  80: 'eighty',
  90: 'ninety',
  1000: 'onethousand'
}

def number_to_written(n):
  if n in lookup:
    return lookup[n]
  else:
    parts = [int(i) for i in str(n)]
    if len(parts) == 3:
      if parts[1] == 0 and parts[2] == 0:
        return lookup[parts[0]] + 'hundred'
      else:
        return lookup[parts[0]] + 'hundredand' + number_to_written((parts[1] * 10) + parts[2])
    else:
      return lookup[parts[0] * 10] + lookup[parts[1]]

count = 0
for n in range(1, 1001):
  count += len(number_to_written(n))

print(count) # 21124
